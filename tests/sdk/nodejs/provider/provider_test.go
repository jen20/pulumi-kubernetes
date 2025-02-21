// Copyright 2016-2019, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package ints

import (
	"testing"

	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"

	"github.com/pulumi/pulumi-kubernetes/provider/v3/pkg/openapi"
	"github.com/pulumi/pulumi-kubernetes/tests/v3"
	"github.com/pulumi/pulumi/pkg/v3/resource/deploy/providers"
	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/stretchr/testify/assert"
)

func TestProvider(t *testing.T) {
	integration.ProgramTest(t, &integration.ProgramTestOptions{
		Dir:          "step1",
		Dependencies: []string{"@pulumi/kubernetes"},
		Quick:        true,
		ExtraRuntimeValidation: func(t *testing.T, stackInfo integration.RuntimeValidationStackInfo) {
			assert.NotNil(t, stackInfo.Deployment)
			assert.Equal(t, 10, len(stackInfo.Deployment.Resources))

			tests.SortResourcesByURN(stackInfo)

			stackRes := stackInfo.Deployment.Resources[9]
			assert.Equal(t, resource.RootStackType, stackRes.URN.Type())

			k8sPathProvider := stackInfo.Deployment.Resources[8]
			assert.True(t, providers.IsProviderType(k8sPathProvider.URN.Type()))

			k8sContentsProvider := stackInfo.Deployment.Resources[7]
			assert.True(t, providers.IsProviderType(k8sContentsProvider.URN.Type()))

			defaultProvider := stackInfo.Deployment.Resources[6]
			assert.True(t, providers.IsProviderType(defaultProvider.URN.Type()))

			// Assert the provider default Namespace (ns1) was created
			ns1 := stackInfo.Deployment.Resources[0]
			assert.Equal(t, tokens.Type("kubernetes:core/v1:Namespace"), ns1.URN.Type())
			providerNsName, _ := openapi.Pluck(ns1.Outputs, "metadata", "name")

			// Assert the ns2 Namespace was created
			ns2 := stackInfo.Deployment.Resources[1]
			assert.Equal(t, tokens.Type("kubernetes:core/v1:Namespace"), ns2.URN.Type())
			ns2Name, _ := openapi.Pluck(ns2.Outputs, "metadata", "name")

			// Assert the other Namespace was created and doesn't use the provider default.
			otherNamespace := stackInfo.Deployment.Resources[2]
			assert.Equal(t, tokens.Type("kubernetes:core/v1:Namespace"), otherNamespace.URN.Type())
			nsName, _ := openapi.Pluck(otherNamespace.Outputs, "metadata", "name")
			assert.NotEqual(t, nsName.(string), providerNsName.(string))

			// Assert the first Pod was created in the provider default namespace.
			pod1 := stackInfo.Deployment.Resources[4]
			assert.Equal(t, "nginx1", string(pod1.URN.Name()))
			podNamespace1, _ := openapi.Pluck(pod1.Outputs, "metadata", "namespace")
			assert.Equal(t, providerNsName.(string), podNamespace1.(string))

			// Assert the second Pod was created in the provider default namespace.
			pod2 := stackInfo.Deployment.Resources[5]
			assert.Equal(t, "nginx2", string(pod2.URN.Name()))
			podNamespace2, _ := openapi.Pluck(pod2.Outputs, "metadata", "namespace")
			assert.Equal(t, providerNsName.(string), podNamespace2.(string))

			// Assert the Pod was created in the specified namespace rather than the provider default namespace.
			namespacedPod := stackInfo.Deployment.Resources[3]
			assert.Equal(t, "namespaced-nginx", string(namespacedPod.URN.Name()))
			namespacedPodNamespace, _ := openapi.Pluck(namespacedPod.Outputs, "metadata", "namespace")
			assert.NotEqual(t, providerNsName.(string), namespacedPodNamespace.(string))
			assert.Equal(t, ns2Name.(string), namespacedPodNamespace.(string))
		},
	})
}
