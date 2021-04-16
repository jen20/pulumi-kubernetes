// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// PodTemplateList is a list of PodTemplates.
type PodTemplateList struct {
	pulumi.CustomResourceState

	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrOutput `pulumi:"apiVersion"`
	// List of pod templates
	Items PodTemplateTypeArrayOutput `pulumi:"items"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrOutput `pulumi:"kind"`
	// Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Metadata metav1.ListMetaPtrOutput `pulumi:"metadata"`
}

// NewPodTemplateList registers a new resource with the given unique name, arguments, and options.
func NewPodTemplateList(ctx *pulumi.Context,
	name string, args *PodTemplateListArgs, opts ...pulumi.ResourceOption) (*PodTemplateList, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Items == nil {
		return nil, errors.New("invalid value for required argument 'Items'")
	}
	args.ApiVersion = pulumi.StringPtr("v1")
	args.Kind = pulumi.StringPtr("PodTemplateList")
	var resource PodTemplateList
	err := ctx.RegisterResource("kubernetes:core/v1:PodTemplateList", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPodTemplateList gets an existing PodTemplateList resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPodTemplateList(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PodTemplateListState, opts ...pulumi.ResourceOption) (*PodTemplateList, error) {
	var resource PodTemplateList
	err := ctx.ReadResource("kubernetes:core/v1:PodTemplateList", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PodTemplateList resources.
type podTemplateListState struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion *string `pulumi:"apiVersion"`
	// List of pod templates
	Items []PodTemplateType `pulumi:"items"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind *string `pulumi:"kind"`
	// Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Metadata *metav1.ListMeta `pulumi:"metadata"`
}

type PodTemplateListState struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrInput
	// List of pod templates
	Items PodTemplateTypeArrayInput
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrInput
	// Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Metadata metav1.ListMetaPtrInput
}

func (PodTemplateListState) ElementType() reflect.Type {
	return reflect.TypeOf((*podTemplateListState)(nil)).Elem()
}

type podTemplateListArgs struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion *string `pulumi:"apiVersion"`
	// List of pod templates
	Items []PodTemplateType `pulumi:"items"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind *string `pulumi:"kind"`
	// Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Metadata *metav1.ListMeta `pulumi:"metadata"`
}

// The set of arguments for constructing a PodTemplateList resource.
type PodTemplateListArgs struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrInput
	// List of pod templates
	Items PodTemplateTypeArrayInput
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrInput
	// Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Metadata metav1.ListMetaPtrInput
}

func (PodTemplateListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*podTemplateListArgs)(nil)).Elem()
}

type PodTemplateListInput interface {
	pulumi.Input

	ToPodTemplateListOutput() PodTemplateListOutput
	ToPodTemplateListOutputWithContext(ctx context.Context) PodTemplateListOutput
}

func (*PodTemplateList) ElementType() reflect.Type {
	return reflect.TypeOf((*PodTemplateList)(nil))
}

func (i *PodTemplateList) ToPodTemplateListOutput() PodTemplateListOutput {
	return i.ToPodTemplateListOutputWithContext(context.Background())
}

func (i *PodTemplateList) ToPodTemplateListOutputWithContext(ctx context.Context) PodTemplateListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PodTemplateListOutput)
}

func (i *PodTemplateList) ToPodTemplateListPtrOutput() PodTemplateListPtrOutput {
	return i.ToPodTemplateListPtrOutputWithContext(context.Background())
}

func (i *PodTemplateList) ToPodTemplateListPtrOutputWithContext(ctx context.Context) PodTemplateListPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PodTemplateListPtrOutput)
}

type PodTemplateListPtrInput interface {
	pulumi.Input

	ToPodTemplateListPtrOutput() PodTemplateListPtrOutput
	ToPodTemplateListPtrOutputWithContext(ctx context.Context) PodTemplateListPtrOutput
}

type podTemplateListPtrType PodTemplateListArgs

func (*podTemplateListPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**PodTemplateList)(nil))
}

func (i *podTemplateListPtrType) ToPodTemplateListPtrOutput() PodTemplateListPtrOutput {
	return i.ToPodTemplateListPtrOutputWithContext(context.Background())
}

func (i *podTemplateListPtrType) ToPodTemplateListPtrOutputWithContext(ctx context.Context) PodTemplateListPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PodTemplateListPtrOutput)
}

// PodTemplateListArrayInput is an input type that accepts PodTemplateListArray and PodTemplateListArrayOutput values.
// You can construct a concrete instance of `PodTemplateListArrayInput` via:
//
//          PodTemplateListArray{ PodTemplateListArgs{...} }
type PodTemplateListArrayInput interface {
	pulumi.Input

	ToPodTemplateListArrayOutput() PodTemplateListArrayOutput
	ToPodTemplateListArrayOutputWithContext(context.Context) PodTemplateListArrayOutput
}

type PodTemplateListArray []PodTemplateListInput

func (PodTemplateListArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*PodTemplateList)(nil))
}

func (i PodTemplateListArray) ToPodTemplateListArrayOutput() PodTemplateListArrayOutput {
	return i.ToPodTemplateListArrayOutputWithContext(context.Background())
}

func (i PodTemplateListArray) ToPodTemplateListArrayOutputWithContext(ctx context.Context) PodTemplateListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PodTemplateListArrayOutput)
}

// PodTemplateListMapInput is an input type that accepts PodTemplateListMap and PodTemplateListMapOutput values.
// You can construct a concrete instance of `PodTemplateListMapInput` via:
//
//          PodTemplateListMap{ "key": PodTemplateListArgs{...} }
type PodTemplateListMapInput interface {
	pulumi.Input

	ToPodTemplateListMapOutput() PodTemplateListMapOutput
	ToPodTemplateListMapOutputWithContext(context.Context) PodTemplateListMapOutput
}

type PodTemplateListMap map[string]PodTemplateListInput

func (PodTemplateListMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*PodTemplateList)(nil))
}

func (i PodTemplateListMap) ToPodTemplateListMapOutput() PodTemplateListMapOutput {
	return i.ToPodTemplateListMapOutputWithContext(context.Background())
}

func (i PodTemplateListMap) ToPodTemplateListMapOutputWithContext(ctx context.Context) PodTemplateListMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PodTemplateListMapOutput)
}

type PodTemplateListOutput struct {
	*pulumi.OutputState
}

func (PodTemplateListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PodTemplateList)(nil))
}

func (o PodTemplateListOutput) ToPodTemplateListOutput() PodTemplateListOutput {
	return o
}

func (o PodTemplateListOutput) ToPodTemplateListOutputWithContext(ctx context.Context) PodTemplateListOutput {
	return o
}

func (o PodTemplateListOutput) ToPodTemplateListPtrOutput() PodTemplateListPtrOutput {
	return o.ToPodTemplateListPtrOutputWithContext(context.Background())
}

func (o PodTemplateListOutput) ToPodTemplateListPtrOutputWithContext(ctx context.Context) PodTemplateListPtrOutput {
	return o.ApplyT(func(v PodTemplateList) *PodTemplateList {
		return &v
	}).(PodTemplateListPtrOutput)
}

type PodTemplateListPtrOutput struct {
	*pulumi.OutputState
}

func (PodTemplateListPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PodTemplateList)(nil))
}

func (o PodTemplateListPtrOutput) ToPodTemplateListPtrOutput() PodTemplateListPtrOutput {
	return o
}

func (o PodTemplateListPtrOutput) ToPodTemplateListPtrOutputWithContext(ctx context.Context) PodTemplateListPtrOutput {
	return o
}

type PodTemplateListArrayOutput struct{ *pulumi.OutputState }

func (PodTemplateListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PodTemplateList)(nil))
}

func (o PodTemplateListArrayOutput) ToPodTemplateListArrayOutput() PodTemplateListArrayOutput {
	return o
}

func (o PodTemplateListArrayOutput) ToPodTemplateListArrayOutputWithContext(ctx context.Context) PodTemplateListArrayOutput {
	return o
}

func (o PodTemplateListArrayOutput) Index(i pulumi.IntInput) PodTemplateListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) PodTemplateList {
		return vs[0].([]PodTemplateList)[vs[1].(int)]
	}).(PodTemplateListOutput)
}

type PodTemplateListMapOutput struct{ *pulumi.OutputState }

func (PodTemplateListMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]PodTemplateList)(nil))
}

func (o PodTemplateListMapOutput) ToPodTemplateListMapOutput() PodTemplateListMapOutput {
	return o
}

func (o PodTemplateListMapOutput) ToPodTemplateListMapOutputWithContext(ctx context.Context) PodTemplateListMapOutput {
	return o
}

func (o PodTemplateListMapOutput) MapIndex(k pulumi.StringInput) PodTemplateListOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) PodTemplateList {
		return vs[0].(map[string]PodTemplateList)[vs[1].(string)]
	}).(PodTemplateListOutput)
}

func init() {
	pulumi.RegisterOutputType(PodTemplateListOutput{})
	pulumi.RegisterOutputType(PodTemplateListPtrOutput{})
	pulumi.RegisterOutputType(PodTemplateListArrayOutput{})
	pulumi.RegisterOutputType(PodTemplateListMapOutput{})
}
