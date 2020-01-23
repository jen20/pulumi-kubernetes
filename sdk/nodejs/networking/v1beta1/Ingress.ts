// *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { core } from "../..";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import { getVersion } from "../../version";

    /**
     * Ingress is a collection of rules that allow inbound connections to reach the endpoints
     * defined by a backend. An Ingress can be configured to give services externally-reachable
     * urls, load balance traffic, terminate SSL, offer name based virtual hosting etc.
     * 
     * This resource waits until its status is ready before registering success
     * for create/update, and populating output properties from the current state of the resource.
     * The following conditions are used to determine whether the resource creation has
     * succeeded or failed:
     * 
     * 1.  Ingress object exists.
     * 2.  Endpoint objects exist with matching names for each Ingress path (except when Service
     *     type is ExternalName).
     * 3.  Ingress entry exists for '.status.loadBalancer.ingress'.
     * 
     * If the Ingress has not reached a Ready state after 10 minutes, it will
     * time out and mark the resource update as Failed. You can override the default timeout value
     * by setting the 'customTimeouts' option on the resource.
     */
    export class Ingress extends pulumi.CustomResource {
      /**
       * APIVersion defines the versioned schema of this representation of an object. Servers should
       * convert recognized schemas to the latest internal value, and may reject unrecognized
       * values. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
       */
      public readonly apiVersion: pulumi.Output<"networking.k8s.io/v1beta1">;

      /**
       * Kind is a string value representing the REST resource this object represents. Servers may
       * infer this from the endpoint the client submits requests to. Cannot be updated. In
       * CamelCase. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
       */
      public readonly kind: pulumi.Output<"Ingress">;

      /**
       * Standard object's metadata. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
       */
      public readonly metadata: pulumi.Output<outputs.meta.v1.ObjectMeta>;

      /**
       * Spec is the desired state of the Ingress. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
       */
      public readonly spec: pulumi.Output<outputs.networking.v1beta1.IngressSpec>;

      /**
       * Status is the current state of the Ingress. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
       */
      public readonly status: pulumi.Output<outputs.networking.v1beta1.IngressStatus>;

      /**
       * Get the state of an existing `Ingress` resource, as identified by `id`.
       * The ID is of the form `[namespace]/<name>`; if `namespace` is omitted, then (per
       * Kubernetes convention) the ID becomes `default/<name>`.
       *
       * Pulumi will keep track of this resource using `name` as the Pulumi ID.
       *
       * @param name _Unique_ name used to register this resource with Pulumi.
       * @param id An ID for the Kubernetes resource to retrieve. Takes the form `[namespace]/<name>`.
       * @param opts Uniquely specifies a CustomResource to select.
       */
      public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Ingress {
          return new Ingress(name, undefined, { ...opts, id: id });
      }

      /** @internal */
      private static readonly __pulumiType = "kubernetes:networking.k8s.io/v1beta1:Ingress";

      /**
       * Returns true if the given object is an instance of Ingress.  This is designed to work even
       * when multiple copies of the Pulumi SDK have been loaded into the same process.
       */
      public static isInstance(obj: any): obj is Ingress {
          if (obj === undefined || obj === null) {
              return false;
          }

          return obj["__pulumiType"] === Ingress.__pulumiType;
      }

      /**
       * Create a networking.v1beta1.Ingress resource with the given unique name, arguments, and options.
       *
       * @param name The _unique_ name of the resource.
       * @param args The arguments to use to populate this resource's properties.
       * @param opts A bag of options that control this resource's behavior.
       */
      constructor(name: string, args?: inputs.networking.v1beta1.Ingress, opts?: pulumi.CustomResourceOptions) {
          const props: pulumi.Inputs = {};

          props["apiVersion"] = "networking.k8s.io/v1beta1";
          props["kind"] = "Ingress";
          props["metadata"] = args?.metadata;
          props["spec"] = args?.spec;

          props["status"] = undefined;

          if (!opts) {
              opts = {};
          }

          if (!opts.version) {
              opts.version = getVersion();
          }

          const _opts = pulumi.mergeOptions(opts, {
              aliases: [
                  { parent: opts.parent, type: "kubernetes:networking/v1beta1:Ingress", name: name },
                  { parent: opts.parent, type: "kubernetes:extensions/v1beta1:Ingress", name: name },
              ],
          });

          super(Ingress.__pulumiType, name, props, _opts);
      }
    }
