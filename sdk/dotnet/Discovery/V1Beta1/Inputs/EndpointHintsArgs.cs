// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Discovery.V1Beta1
{

    /// <summary>
    /// EndpointHints provides hints describing how an endpoint should be consumed.
    /// </summary>
    public class EndpointHintsArgs : Pulumi.ResourceArgs
    {
        [Input("forZones")]
        private InputList<Pulumi.Kubernetes.Types.Inputs.Discovery.V1Beta1.ForZoneArgs>? _forZones;

        /// <summary>
        /// forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing. May contain a maximum of 8 entries.
        /// </summary>
        public InputList<Pulumi.Kubernetes.Types.Inputs.Discovery.V1Beta1.ForZoneArgs> ForZones
        {
            get => _forZones ?? (_forZones = new InputList<Pulumi.Kubernetes.Types.Inputs.Discovery.V1Beta1.ForZoneArgs>());
            set => _forZones = value;
        }

        public EndpointHintsArgs()
        {
        }
    }
}