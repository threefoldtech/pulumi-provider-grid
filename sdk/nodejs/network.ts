// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Network extends pulumi.CustomResource {
    /**
     * Get an existing Network resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Network {
        return new Network(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'threefold:index:Network';

    /**
     * Returns true if the given object is an instance of Network.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Network {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Network.__pulumiType;
    }

    /**
     * Generated wireguard configuration for external user access to the network
     */
    public /*out*/ readonly access_wg_config!: pulumi.Output<string>;
    /**
     * A flag to support wireguard in the network
     */
    public readonly add_wg_access!: pulumi.Output<boolean | undefined>;
    /**
     * The description of the network workload, optional with no restrictions
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * Wireguard IP assigned for external user access
     */
    public /*out*/ readonly external_ip!: pulumi.Output<string>;
    /**
     * External user private key used in encryption while communicating through Wireguard network
     */
    public /*out*/ readonly external_sk!: pulumi.Output<string>;
    /**
     * The IP range for the network, subnet should be 16
     */
    public readonly ip_range!: pulumi.Output<string>;
    /**
     * A flag to generate a random mycelium key to support mycelium in the network
     */
    public readonly mycelium!: pulumi.Output<boolean | undefined>;
    /**
     * A map of nodes as a key and mycelium key for each node, mycelium key length should be 32. Selected nodes must be included in the network's nodes
     */
    public readonly mycelium_keys!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The name of the network workload, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Mapping from each node to its deployment id
     */
    public /*out*/ readonly node_deployment_id!: pulumi.Output<{[key: string]: number}>;
    /**
     * The nodes used to deploy the network on, shouldn't be empty
     */
    public readonly nodes!: pulumi.Output<any[]>;
    /**
     * Computed values of nodes' IP ranges after deployment
     */
    public /*out*/ readonly nodes_ip_range!: pulumi.Output<{[key: string]: string}>;
    /**
     * Public node id (in case it's added). Used for wireguard access and supporting hidden nodes
     */
    public /*out*/ readonly public_node_id!: pulumi.Output<number>;
    /**
     * The solution type of the network, displayed as project name in contract metadata
     */
    public readonly solution_type!: pulumi.Output<string | undefined>;

    /**
     * Create a Network resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.ip_range === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ip_range'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.nodes === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nodes'");
            }
            resourceInputs["add_wg_access"] = args ? args.add_wg_access : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["ip_range"] = args ? args.ip_range : undefined;
            resourceInputs["mycelium"] = args ? args.mycelium : undefined;
            resourceInputs["mycelium_keys"] = args ? args.mycelium_keys : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nodes"] = args ? args.nodes : undefined;
            resourceInputs["solution_type"] = (args ? args.solution_type : undefined) ?? "Network";
            resourceInputs["access_wg_config"] = undefined /*out*/;
            resourceInputs["external_ip"] = undefined /*out*/;
            resourceInputs["external_sk"] = undefined /*out*/;
            resourceInputs["node_deployment_id"] = undefined /*out*/;
            resourceInputs["nodes_ip_range"] = undefined /*out*/;
            resourceInputs["public_node_id"] = undefined /*out*/;
        } else {
            resourceInputs["access_wg_config"] = undefined /*out*/;
            resourceInputs["add_wg_access"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["external_ip"] = undefined /*out*/;
            resourceInputs["external_sk"] = undefined /*out*/;
            resourceInputs["ip_range"] = undefined /*out*/;
            resourceInputs["mycelium"] = undefined /*out*/;
            resourceInputs["mycelium_keys"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["node_deployment_id"] = undefined /*out*/;
            resourceInputs["nodes"] = undefined /*out*/;
            resourceInputs["nodes_ip_range"] = undefined /*out*/;
            resourceInputs["public_node_id"] = undefined /*out*/;
            resourceInputs["solution_type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Network.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Network resource.
 */
export interface NetworkArgs {
    /**
     * A flag to support wireguard in the network
     */
    add_wg_access?: pulumi.Input<boolean>;
    /**
     * The description of the network workload, optional with no restrictions
     */
    description: pulumi.Input<string>;
    /**
     * The IP range for the network, subnet should be 16
     */
    ip_range: pulumi.Input<string>;
    /**
     * A flag to generate a random mycelium key to support mycelium in the network
     */
    mycelium?: pulumi.Input<boolean>;
    /**
     * A map of nodes as a key and mycelium key for each node, mycelium key length should be 32. Selected nodes must be included in the network's nodes
     */
    mycelium_keys?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The name of the network workload, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported
     */
    name: pulumi.Input<string>;
    /**
     * The nodes used to deploy the network on, shouldn't be empty
     */
    nodes: pulumi.Input<any[]>;
    /**
     * The solution type of the network, displayed as project name in contract metadata
     */
    solution_type?: pulumi.Input<string>;
}
