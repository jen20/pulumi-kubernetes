package provider

import (
	"encoding/json"
	"fmt"
	"strings"

	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/apis/meta/v1/unstructured"
	"k8s.io/client-go/tools/clientcmd"
	clientapi "k8s.io/client-go/tools/clientcmd/api"
)

func hasComputedValue(obj *unstructured.Unstructured) bool {
	if obj == nil || obj.Object == nil {
		return false
	}

	objects := []map[string]interface{}{obj.Object}
	var curr map[string]interface{}

	for {
		if len(objects) == 0 {
			break
		}
		curr, objects = objects[0], objects[1:]
		for _, v := range curr {
			switch field := v.(type) {
			case resource.Computed:
				return true
			case map[string]interface{}:
				objects = append(objects, field)
			case []interface{}:
				for _, v := range field {
					objects = append(objects, map[string]interface{}{"": v})
				}
			case []map[string]interface{}:
				objects = append(objects, field...)
			}
		}
	}

	return false
}

// --------------------------------------------------------------------------
// Names and namespaces.
// --------------------------------------------------------------------------

// fqObjName returns "namespace.name"
func fqObjName(o metav1.Object) string {
	return fqName(o.GetNamespace(), o.GetName())
}

// parseFqName will parse a fully-qualified Kubernetes object name.
func parseFqName(id string) (namespace, name string) {
	split := strings.Split(id, "/")
	if len(split) == 1 {
		return "", split[0]
	}
	namespace, name = split[0], split[1]
	return
}

// fqName returns "namespace/name"
func fqName(namespace, name string) string {
	if namespace == "" {
		return name
	}
	return fmt.Sprintf("%s/%s", namespace, name)
}

// --------------------------------------------------------------------------
// Kubeconfig helpers.
// --------------------------------------------------------------------------

// parseKubeconfigPropertyValue takes a PropertyValue that possibly contains a raw kubeconfig
// (YAML or JSON) string or map and attempts to unmarshal it into a Config struct. If the property value
// is empty, an empty Config is returned.
func parseKubeconfigPropertyValue(kubeconfig resource.PropertyValue) (*clientapi.Config, error) {
	if kubeconfig.IsNull() {
		return &clientapi.Config{}, nil
	}

	var cfg []byte
	if kubeconfig.IsString() {
		cfg = []byte(kubeconfig.StringValue())
	} else if kubeconfig.IsObject() {
		raw := kubeconfig.ObjectValue().Mappable()
		jsonBytes, err := json.Marshal(raw)
		if err != nil {
			return nil, fmt.Errorf("failed to unmarshal kubeconfig: %v", err)
		}
		cfg = jsonBytes
	} else {
		return nil, fmt.Errorf("unexpected kubeconfig format, type: %v", kubeconfig.TypeString())
	}
	config, err := clientcmd.Load(cfg)
	if err != nil {
		return nil, fmt.Errorf("failed to parse kubeconfig: %v", err)
	}

	return config, nil
}

// getActiveClusterFromConfig gets the current cluster from a kubeconfig, accounting for provider overrides.
func getActiveClusterFromConfig(config *clientapi.Config, overrides resource.PropertyMap) *clientapi.Cluster {
	if len(config.Clusters) == 0 {
		return &clientapi.Cluster{}
	}

	currentContext := config.CurrentContext
	if val := overrides["context"]; !val.IsNull() {
		currentContext = val.StringValue()
	}

	activeClusterName := config.Contexts[currentContext].Cluster

	activeCluster := config.Clusters[activeClusterName]
	if val := overrides["cluster"]; !val.IsNull() {
		activeCluster = config.Clusters[val.StringValue()]
	}

	return activeCluster
}
