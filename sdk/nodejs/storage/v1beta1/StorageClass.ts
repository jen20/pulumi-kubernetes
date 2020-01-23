// *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { core } from "../..";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import { getVersion } from "../../version";

    /**
     * StorageClass describes the parameters for a class of storage for which PersistentVolumes can
     * be dynamically provisioned.
     * 
     * StorageClasses are non-namespaced; the name of the storage class according to etcd is in
     * ObjectMeta.Name.
     */
    export class StorageClass extends pulumi.CustomResource {
      /**
       * AllowVolumeExpansion shows whether the storage class allow volume expand
       */
      public readonly allowVolumeExpansion: pulumi.Output<boolean>;

      /**
       * Restrict the node topologies where volumes can be dynamically provisioned. Each volume
       * plugin defines its own supported topology specifications. An empty TopologySelectorTerm
       * list means there is no topology restriction. This field is only honored by servers that
       * enable the VolumeScheduling feature.
       */
      public readonly allowedTopologies: pulumi.Output<outputs.core.v1.TopologySelectorTerm[]>;

      /**
       * APIVersion defines the versioned schema of this representation of an object. Servers should
       * convert recognized schemas to the latest internal value, and may reject unrecognized
       * values. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
       */
      public readonly apiVersion: pulumi.Output<"storage.k8s.io/v1beta1">;

      /**
       * Kind is a string value representing the REST resource this object represents. Servers may
       * infer this from the endpoint the client submits requests to. Cannot be updated. In
       * CamelCase. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
       */
      public readonly kind: pulumi.Output<"StorageClass">;

      /**
       * Standard object's metadata. More info:
       * https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
       */
      public readonly metadata: pulumi.Output<outputs.meta.v1.ObjectMeta>;

      /**
       * Dynamically provisioned PersistentVolumes of this storage class are created with these
       * mountOptions, e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one
       * is invalid.
       */
      public readonly mountOptions: pulumi.Output<string[]>;

      /**
       * Parameters holds the parameters for the provisioner that should create volumes of this
       * storage class.
       */
      public readonly parameters: pulumi.Output<{[key: string]: pulumi.Output<string>}>;

      /**
       * Provisioner indicates the type of the provisioner.
       */
      public readonly provisioner: pulumi.Output<string>;

      /**
       * Dynamically provisioned PersistentVolumes of this storage class are created with this
       * reclaimPolicy. Defaults to Delete.
       */
      public readonly reclaimPolicy: pulumi.Output<string>;

      /**
       * VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.
       * When unset, VolumeBindingImmediate is used. This field is only honored by servers that
       * enable the VolumeScheduling feature.
       */
      public readonly volumeBindingMode: pulumi.Output<string>;

      /**
       * Get the state of an existing `StorageClass` resource, as identified by `id`.
       * The ID is of the form `[namespace]/<name>`; if `namespace` is omitted, then (per
       * Kubernetes convention) the ID becomes `default/<name>`.
       *
       * Pulumi will keep track of this resource using `name` as the Pulumi ID.
       *
       * @param name _Unique_ name used to register this resource with Pulumi.
       * @param id An ID for the Kubernetes resource to retrieve. Takes the form `[namespace]/<name>`.
       * @param opts Uniquely specifies a CustomResource to select.
       */
      public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): StorageClass {
          return new StorageClass(name, undefined, { ...opts, id: id });
      }

      /** @internal */
      private static readonly __pulumiType = "kubernetes:storage.k8s.io/v1beta1:StorageClass";

      /**
       * Returns true if the given object is an instance of StorageClass.  This is designed to work even
       * when multiple copies of the Pulumi SDK have been loaded into the same process.
       */
      public static isInstance(obj: any): obj is StorageClass {
          if (obj === undefined || obj === null) {
              return false;
          }

          return obj["__pulumiType"] === StorageClass.__pulumiType;
      }

      /**
       * Create a storage.v1beta1.StorageClass resource with the given unique name, arguments, and options.
       *
       * @param name The _unique_ name of the resource.
       * @param args The arguments to use to populate this resource's properties.
       * @param opts A bag of options that control this resource's behavior.
       */
      constructor(name: string, args?: inputs.storage.v1beta1.StorageClass, opts?: pulumi.CustomResourceOptions) {
          const props: pulumi.Inputs = {};
          props["provisioner"] = args?.provisioner;

          props["allowVolumeExpansion"] = args?.allowVolumeExpansion;
          props["allowedTopologies"] = args?.allowedTopologies;
          props["apiVersion"] = "storage.k8s.io/v1beta1";
          props["kind"] = "StorageClass";
          props["metadata"] = args?.metadata;
          props["mountOptions"] = args?.mountOptions;
          props["parameters"] = args?.parameters;
          props["reclaimPolicy"] = args?.reclaimPolicy;
          props["volumeBindingMode"] = args?.volumeBindingMode;

          props["status"] = undefined;

          if (!opts) {
              opts = {};
          }

          if (!opts.version) {
              opts.version = getVersion();
          }

          super(StorageClass.__pulumiType, name, props, opts);
      }
    }
