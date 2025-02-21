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

	"github.com/pulumi/pulumi-kubernetes/provider/v3/pkg/openapi"
	"github.com/pulumi/pulumi-kubernetes/tests/v3"
	"github.com/pulumi/pulumi/pkg/v3/resource/deploy/providers"
	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/stretchr/testify/assert"
)

func TestGet(t *testing.T) {
	integration.ProgramTest(t, &integration.ProgramTestOptions{
		Dir:                  "step1",
		Dependencies:         []string{"@pulumi/kubernetes"},
		Quick:                true,
		ExpectRefreshChanges: true,
		ExtraRuntimeValidation: func(t *testing.T, stackInfo integration.RuntimeValidationStackInfo) {
			assert.NotNil(t, stackInfo.Deployment)
			assert.Equal(t, 6, len(stackInfo.Deployment.Resources))

			tests.SortResourcesByURN(stackInfo)

			stackRes := stackInfo.Deployment.Resources[5]
			assert.Equal(t, resource.RootStackType, stackRes.URN.Type())

			provRes := stackInfo.Deployment.Resources[4]
			assert.True(t, providers.IsProviderType(provRes.URN.Type()))

			//
			// Assert we can use .get to retrieve the kube-api Service.
			//

			service := stackInfo.Deployment.Resources[2]
			assert.Equal(t, "kube-api", string(service.URN.Name()))
			step1Name, _ := openapi.Pluck(service.Outputs, "metadata", "name")
			assert.Equal(t, "kubernetes", step1Name.(string))

			//
			// Assert that CRD and CR exist
			//

			crd := stackInfo.Deployment.Resources[0]
			assert.Equal(t, "crontab", string(crd.URN.Name()))

			ct1 := stackInfo.Deployment.Resources[3]
			assert.Equal(t, "my-new-cron-object", string(ct1.URN.Name()))

		},
		EditDirs: []integration.EditDir{
			{
				Dir:      "step2",
				Additive: true,
				ExtraRuntimeValidation: func(t *testing.T, stackInfo integration.RuntimeValidationStackInfo) {
					assert.NotNil(t, stackInfo.Deployment)
					assert.Equal(t, 7, len(stackInfo.Deployment.Resources))

					tests.SortResourcesByURN(stackInfo)

					stackRes := stackInfo.Deployment.Resources[6]
					assert.Equal(t, resource.RootStackType, stackRes.URN.Type())

					provRes := stackInfo.Deployment.Resources[5]
					assert.True(t, providers.IsProviderType(provRes.URN.Type()))

					//
					// Assert we can use .get to retrieve CRDs.
					//

					ct2 := stackInfo.Deployment.Resources[4]
					assert.Equal(t, "my-new-cron-object-get", string(ct2.URN.Name()))
					image, _ := openapi.Pluck(ct2.Outputs, "spec", "image")
					assert.Equal(t, "my-awesome-cron-image", image.(string))
				},
			},
		},
	})
}
