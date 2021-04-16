// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// EndpointSliceList represents a list of endpoint slices
type EndpointSliceList struct {
	pulumi.CustomResourceState

	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrOutput `pulumi:"apiVersion"`
	// List of endpoint slices
	Items EndpointSliceTypeArrayOutput `pulumi:"items"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrOutput `pulumi:"kind"`
	// Standard list metadata.
	Metadata metav1.ListMetaPtrOutput `pulumi:"metadata"`
}

// NewEndpointSliceList registers a new resource with the given unique name, arguments, and options.
func NewEndpointSliceList(ctx *pulumi.Context,
	name string, args *EndpointSliceListArgs, opts ...pulumi.ResourceOption) (*EndpointSliceList, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Items == nil {
		return nil, errors.New("invalid value for required argument 'Items'")
	}
	args.ApiVersion = pulumi.StringPtr("discovery.k8s.io/v1beta1")
	args.Kind = pulumi.StringPtr("EndpointSliceList")
	var resource EndpointSliceList
	err := ctx.RegisterResource("kubernetes:discovery.k8s.io/v1beta1:EndpointSliceList", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEndpointSliceList gets an existing EndpointSliceList resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEndpointSliceList(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EndpointSliceListState, opts ...pulumi.ResourceOption) (*EndpointSliceList, error) {
	var resource EndpointSliceList
	err := ctx.ReadResource("kubernetes:discovery.k8s.io/v1beta1:EndpointSliceList", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EndpointSliceList resources.
type endpointSliceListState struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion *string `pulumi:"apiVersion"`
	// List of endpoint slices
	Items []EndpointSliceType `pulumi:"items"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind *string `pulumi:"kind"`
	// Standard list metadata.
	Metadata *metav1.ListMeta `pulumi:"metadata"`
}

type EndpointSliceListState struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrInput
	// List of endpoint slices
	Items EndpointSliceTypeArrayInput
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrInput
	// Standard list metadata.
	Metadata metav1.ListMetaPtrInput
}

func (EndpointSliceListState) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointSliceListState)(nil)).Elem()
}

type endpointSliceListArgs struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion *string `pulumi:"apiVersion"`
	// List of endpoint slices
	Items []EndpointSliceType `pulumi:"items"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind *string `pulumi:"kind"`
	// Standard list metadata.
	Metadata *metav1.ListMeta `pulumi:"metadata"`
}

// The set of arguments for constructing a EndpointSliceList resource.
type EndpointSliceListArgs struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrInput
	// List of endpoint slices
	Items EndpointSliceTypeArrayInput
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrInput
	// Standard list metadata.
	Metadata metav1.ListMetaPtrInput
}

func (EndpointSliceListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointSliceListArgs)(nil)).Elem()
}

type EndpointSliceListInput interface {
	pulumi.Input

	ToEndpointSliceListOutput() EndpointSliceListOutput
	ToEndpointSliceListOutputWithContext(ctx context.Context) EndpointSliceListOutput
}

func (*EndpointSliceList) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointSliceList)(nil))
}

func (i *EndpointSliceList) ToEndpointSliceListOutput() EndpointSliceListOutput {
	return i.ToEndpointSliceListOutputWithContext(context.Background())
}

func (i *EndpointSliceList) ToEndpointSliceListOutputWithContext(ctx context.Context) EndpointSliceListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointSliceListOutput)
}

func (i *EndpointSliceList) ToEndpointSliceListPtrOutput() EndpointSliceListPtrOutput {
	return i.ToEndpointSliceListPtrOutputWithContext(context.Background())
}

func (i *EndpointSliceList) ToEndpointSliceListPtrOutputWithContext(ctx context.Context) EndpointSliceListPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointSliceListPtrOutput)
}

type EndpointSliceListPtrInput interface {
	pulumi.Input

	ToEndpointSliceListPtrOutput() EndpointSliceListPtrOutput
	ToEndpointSliceListPtrOutputWithContext(ctx context.Context) EndpointSliceListPtrOutput
}

type endpointSliceListPtrType EndpointSliceListArgs

func (*endpointSliceListPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**EndpointSliceList)(nil))
}

func (i *endpointSliceListPtrType) ToEndpointSliceListPtrOutput() EndpointSliceListPtrOutput {
	return i.ToEndpointSliceListPtrOutputWithContext(context.Background())
}

func (i *endpointSliceListPtrType) ToEndpointSliceListPtrOutputWithContext(ctx context.Context) EndpointSliceListPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointSliceListPtrOutput)
}

// EndpointSliceListArrayInput is an input type that accepts EndpointSliceListArray and EndpointSliceListArrayOutput values.
// You can construct a concrete instance of `EndpointSliceListArrayInput` via:
//
//          EndpointSliceListArray{ EndpointSliceListArgs{...} }
type EndpointSliceListArrayInput interface {
	pulumi.Input

	ToEndpointSliceListArrayOutput() EndpointSliceListArrayOutput
	ToEndpointSliceListArrayOutputWithContext(context.Context) EndpointSliceListArrayOutput
}

type EndpointSliceListArray []EndpointSliceListInput

func (EndpointSliceListArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*EndpointSliceList)(nil))
}

func (i EndpointSliceListArray) ToEndpointSliceListArrayOutput() EndpointSliceListArrayOutput {
	return i.ToEndpointSliceListArrayOutputWithContext(context.Background())
}

func (i EndpointSliceListArray) ToEndpointSliceListArrayOutputWithContext(ctx context.Context) EndpointSliceListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointSliceListArrayOutput)
}

// EndpointSliceListMapInput is an input type that accepts EndpointSliceListMap and EndpointSliceListMapOutput values.
// You can construct a concrete instance of `EndpointSliceListMapInput` via:
//
//          EndpointSliceListMap{ "key": EndpointSliceListArgs{...} }
type EndpointSliceListMapInput interface {
	pulumi.Input

	ToEndpointSliceListMapOutput() EndpointSliceListMapOutput
	ToEndpointSliceListMapOutputWithContext(context.Context) EndpointSliceListMapOutput
}

type EndpointSliceListMap map[string]EndpointSliceListInput

func (EndpointSliceListMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*EndpointSliceList)(nil))
}

func (i EndpointSliceListMap) ToEndpointSliceListMapOutput() EndpointSliceListMapOutput {
	return i.ToEndpointSliceListMapOutputWithContext(context.Background())
}

func (i EndpointSliceListMap) ToEndpointSliceListMapOutputWithContext(ctx context.Context) EndpointSliceListMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointSliceListMapOutput)
}

type EndpointSliceListOutput struct {
	*pulumi.OutputState
}

func (EndpointSliceListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointSliceList)(nil))
}

func (o EndpointSliceListOutput) ToEndpointSliceListOutput() EndpointSliceListOutput {
	return o
}

func (o EndpointSliceListOutput) ToEndpointSliceListOutputWithContext(ctx context.Context) EndpointSliceListOutput {
	return o
}

func (o EndpointSliceListOutput) ToEndpointSliceListPtrOutput() EndpointSliceListPtrOutput {
	return o.ToEndpointSliceListPtrOutputWithContext(context.Background())
}

func (o EndpointSliceListOutput) ToEndpointSliceListPtrOutputWithContext(ctx context.Context) EndpointSliceListPtrOutput {
	return o.ApplyT(func(v EndpointSliceList) *EndpointSliceList {
		return &v
	}).(EndpointSliceListPtrOutput)
}

type EndpointSliceListPtrOutput struct {
	*pulumi.OutputState
}

func (EndpointSliceListPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EndpointSliceList)(nil))
}

func (o EndpointSliceListPtrOutput) ToEndpointSliceListPtrOutput() EndpointSliceListPtrOutput {
	return o
}

func (o EndpointSliceListPtrOutput) ToEndpointSliceListPtrOutputWithContext(ctx context.Context) EndpointSliceListPtrOutput {
	return o
}

type EndpointSliceListArrayOutput struct{ *pulumi.OutputState }

func (EndpointSliceListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointSliceList)(nil))
}

func (o EndpointSliceListArrayOutput) ToEndpointSliceListArrayOutput() EndpointSliceListArrayOutput {
	return o
}

func (o EndpointSliceListArrayOutput) ToEndpointSliceListArrayOutputWithContext(ctx context.Context) EndpointSliceListArrayOutput {
	return o
}

func (o EndpointSliceListArrayOutput) Index(i pulumi.IntInput) EndpointSliceListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EndpointSliceList {
		return vs[0].([]EndpointSliceList)[vs[1].(int)]
	}).(EndpointSliceListOutput)
}

type EndpointSliceListMapOutput struct{ *pulumi.OutputState }

func (EndpointSliceListMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]EndpointSliceList)(nil))
}

func (o EndpointSliceListMapOutput) ToEndpointSliceListMapOutput() EndpointSliceListMapOutput {
	return o
}

func (o EndpointSliceListMapOutput) ToEndpointSliceListMapOutputWithContext(ctx context.Context) EndpointSliceListMapOutput {
	return o
}

func (o EndpointSliceListMapOutput) MapIndex(k pulumi.StringInput) EndpointSliceListOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) EndpointSliceList {
		return vs[0].(map[string]EndpointSliceList)[vs[1].(string)]
	}).(EndpointSliceListOutput)
}

func init() {
	pulumi.RegisterOutputType(EndpointSliceListOutput{})
	pulumi.RegisterOutputType(EndpointSliceListPtrOutput{})
	pulumi.RegisterOutputType(EndpointSliceListArrayOutput{})
	pulumi.RegisterOutputType(EndpointSliceListMapOutput{})
}
