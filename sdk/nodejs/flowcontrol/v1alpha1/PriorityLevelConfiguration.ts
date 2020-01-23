// *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { core } from "../..";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import { getVersion } from "../../version";

    /**
     * PriorityLevelConfiguration represents the configuration of a priority level.
     */
    export class PriorityLevelConfiguration extends pulumi.CustomResource {
      /**
       * APIVersion defines the versioned schema of this representation of an object. Servers should
       * convert recognized schemas to the latest internal value, and may reject unrecognized
       * values. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
       */
      public readonly apiVersion: pulumi.Output<"flowcontrol.apiserver.k8s.io/v1alpha1">;

      /**
       * Kind is a string value representing the REST resource this object represents. Servers may
       * infer this from the endpoint the client submits requests to. Cannot be updated. In
       * CamelCase. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
       */
      public readonly kind: pulumi.Output<"PriorityLevelConfiguration">;

      /**
       * `metadata` is the standard object's metadata. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
       */
      public readonly metadata: pulumi.Output<outputs.meta.v1.ObjectMeta>;

      /**
       * `spec` is the specification of the desired behavior of a "request-priority". More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
       */
      public readonly spec: pulumi.Output<outputs.flowcontrol.v1alpha1.PriorityLevelConfigurationSpec>;

      /**
       * `status` is the current status of a "request-priority". More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
       */
      public readonly status: pulumi.Output<outputs.flowcontrol.v1alpha1.PriorityLevelConfigurationStatus>;

      /**
       * Get the state of an existing `PriorityLevelConfiguration` resource, as identified by `id`.
       * The ID is of the form `[namespace]/<name>`; if `namespace` is omitted, then (per
       * Kubernetes convention) the ID becomes `default/<name>`.
       *
       * Pulumi will keep track of this resource using `name` as the Pulumi ID.
       *
       * @param name _Unique_ name used to register this resource with Pulumi.
       * @param id An ID for the Kubernetes resource to retrieve. Takes the form `[namespace]/<name>`.
       * @param opts Uniquely specifies a CustomResource to select.
       */
      public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PriorityLevelConfiguration {
          return new PriorityLevelConfiguration(name, undefined, { ...opts, id: id });
      }

      /** @internal */
      private static readonly __pulumiType = "kubernetes:flowcontrol.apiserver.k8s.io/v1alpha1:PriorityLevelConfiguration";

      /**
       * Returns true if the given object is an instance of PriorityLevelConfiguration.  This is designed to work even
       * when multiple copies of the Pulumi SDK have been loaded into the same process.
       */
      public static isInstance(obj: any): obj is PriorityLevelConfiguration {
          if (obj === undefined || obj === null) {
              return false;
          }

          return obj["__pulumiType"] === PriorityLevelConfiguration.__pulumiType;
      }

      /**
       * Create a flowcontrol.v1alpha1.PriorityLevelConfiguration resource with the given unique name, arguments, and options.
       *
       * @param name The _unique_ name of the resource.
       * @param args The arguments to use to populate this resource's properties.
       * @param opts A bag of options that control this resource's behavior.
       */
      constructor(name: string, args?: inputs.flowcontrol.v1alpha1.PriorityLevelConfiguration, opts?: pulumi.CustomResourceOptions) {
          const props: pulumi.Inputs = {};

          props["apiVersion"] = "flowcontrol.apiserver.k8s.io/v1alpha1";
          props["kind"] = "PriorityLevelConfiguration";
          props["metadata"] = args?.metadata;
          props["spec"] = args?.spec;

          props["status"] = undefined;

          if (!opts) {
              opts = {};
          }

          if (!opts.version) {
              opts.version = getVersion();
          }

          super(PriorityLevelConfiguration.__pulumiType, name, props, opts);
      }
    }
