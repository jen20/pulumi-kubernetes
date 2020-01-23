// *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { core } from "../..";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import { getVersion } from "../../version";

    /**
     * RoleBindingList is a collection of RoleBindings Deprecated in v1.17 in favor of
     * rbac.authorization.k8s.io/v1 RoleBindingList, and will no longer be served in v1.20.
     */
    export class RoleBindingList extends pulumi.CustomResource {
      /**
       * APIVersion defines the versioned schema of this representation of an object. Servers should
       * convert recognized schemas to the latest internal value, and may reject unrecognized
       * values. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
       */
      public readonly apiVersion: pulumi.Output<"rbac.authorization.k8s.io/v1beta1">;

      /**
       * Items is a list of RoleBindings
       */
      public readonly items: pulumi.Output<outputs.rbac.v1beta1.RoleBinding[]>;

      /**
       * Kind is a string value representing the REST resource this object represents. Servers may
       * infer this from the endpoint the client submits requests to. Cannot be updated. In
       * CamelCase. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
       */
      public readonly kind: pulumi.Output<"RoleBindingList">;

      /**
       * Standard object's metadata.
       */
      public readonly metadata: pulumi.Output<outputs.meta.v1.ListMeta>;

      /**
       * Get the state of an existing `RoleBindingList` resource, as identified by `id`.
       * The ID is of the form `[namespace]/<name>`; if `namespace` is omitted, then (per
       * Kubernetes convention) the ID becomes `default/<name>`.
       *
       * Pulumi will keep track of this resource using `name` as the Pulumi ID.
       *
       * @param name _Unique_ name used to register this resource with Pulumi.
       * @param id An ID for the Kubernetes resource to retrieve. Takes the form `[namespace]/<name>`.
       * @param opts Uniquely specifies a CustomResource to select.
       */
      public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): RoleBindingList {
          return new RoleBindingList(name, undefined, { ...opts, id: id });
      }

      /** @internal */
      private static readonly __pulumiType = "kubernetes:rbac.authorization.k8s.io/v1beta1:RoleBindingList";

      /**
       * Returns true if the given object is an instance of RoleBindingList.  This is designed to work even
       * when multiple copies of the Pulumi SDK have been loaded into the same process.
       */
      public static isInstance(obj: any): obj is RoleBindingList {
          if (obj === undefined || obj === null) {
              return false;
          }

          return obj["__pulumiType"] === RoleBindingList.__pulumiType;
      }

      /**
       * Create a rbac.v1beta1.RoleBindingList resource with the given unique name, arguments, and options.
       *
       * @param name The _unique_ name of the resource.
       * @param args The arguments to use to populate this resource's properties.
       * @param opts A bag of options that control this resource's behavior.
       */
      constructor(name: string, args?: inputs.rbac.v1beta1.RoleBindingList, opts?: pulumi.CustomResourceOptions) {
          const props: pulumi.Inputs = {};
          props["items"] = args?.items;

          props["apiVersion"] = "rbac.authorization.k8s.io/v1beta1";
          props["kind"] = "RoleBindingList";
          props["metadata"] = args?.metadata;

          props["status"] = undefined;

          if (!opts) {
              opts = {};
          }

          if (!opts.version) {
              opts.version = getVersion();
          }

          super(RoleBindingList.__pulumiType, name, props, opts);
      }
    }
