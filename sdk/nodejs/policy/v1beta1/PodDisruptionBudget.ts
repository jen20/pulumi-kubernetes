// *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { core } from "../..";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import { getVersion } from "../../version";

    /**
     * PodDisruptionBudget is an object to define the max disruption that can be caused to a
     * collection of pods
     */
    export class PodDisruptionBudget extends pulumi.CustomResource {
      /**
       * APIVersion defines the versioned schema of this representation of an object. Servers should
       * convert recognized schemas to the latest internal value, and may reject unrecognized
       * values. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
       */
      public readonly apiVersion: pulumi.Output<"policy/v1beta1">;

      /**
       * Kind is a string value representing the REST resource this object represents. Servers may
       * infer this from the endpoint the client submits requests to. Cannot be updated. In
       * CamelCase. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
       */
      public readonly kind: pulumi.Output<"PodDisruptionBudget">;

      
      public readonly metadata: pulumi.Output<outputs.meta.v1.ObjectMeta>;

      /**
       * Specification of the desired behavior of the PodDisruptionBudget.
       */
      public readonly spec: pulumi.Output<outputs.policy.v1beta1.PodDisruptionBudgetSpec>;

      /**
       * Most recently observed status of the PodDisruptionBudget.
       */
      public readonly status: pulumi.Output<outputs.policy.v1beta1.PodDisruptionBudgetStatus>;

      /**
       * Get the state of an existing `PodDisruptionBudget` resource, as identified by `id`.
       * The ID is of the form `[namespace]/<name>`; if `namespace` is omitted, then (per
       * Kubernetes convention) the ID becomes `default/<name>`.
       *
       * Pulumi will keep track of this resource using `name` as the Pulumi ID.
       *
       * @param name _Unique_ name used to register this resource with Pulumi.
       * @param id An ID for the Kubernetes resource to retrieve. Takes the form `[namespace]/<name>`.
       * @param opts Uniquely specifies a CustomResource to select.
       */
      public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PodDisruptionBudget {
          return new PodDisruptionBudget(name, undefined, { ...opts, id: id });
      }

      /** @internal */
      private static readonly __pulumiType = "kubernetes:policy/v1beta1:PodDisruptionBudget";

      /**
       * Returns true if the given object is an instance of PodDisruptionBudget.  This is designed to work even
       * when multiple copies of the Pulumi SDK have been loaded into the same process.
       */
      public static isInstance(obj: any): obj is PodDisruptionBudget {
          if (obj === undefined || obj === null) {
              return false;
          }

          return obj["__pulumiType"] === PodDisruptionBudget.__pulumiType;
      }

      /**
       * Create a policy.v1beta1.PodDisruptionBudget resource with the given unique name, arguments, and options.
       *
       * @param name The _unique_ name of the resource.
       * @param args The arguments to use to populate this resource's properties.
       * @param opts A bag of options that control this resource's behavior.
       */
      constructor(name: string, args?: inputs.policy.v1beta1.PodDisruptionBudget, opts?: pulumi.CustomResourceOptions) {
          const props: pulumi.Inputs = {};

          props["apiVersion"] = "policy/v1beta1";
          props["kind"] = "PodDisruptionBudget";
          props["metadata"] = args?.metadata;
          props["spec"] = args?.spec;

          props["status"] = undefined;

          if (!opts) {
              opts = {};
          }

          if (!opts.version) {
              opts.version = getVersion();
          }

          super(PodDisruptionBudget.__pulumiType, name, props, opts);
      }
    }
