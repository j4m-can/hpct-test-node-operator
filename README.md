# hpct-head-node-operator

## Description

Test node operator acting as principal for subordinate charms.

## Usage

To deploy:

```
juju deploy ./hpct-test-node-operator_ubuntu-22.04-amd64.charm
```

Assuming a `hpct-test-subordinate-operator` has been deployed:

```
juju relate hpct-test-node-operator hpct-test-subordinate-operator
```

## Relations

A "ready" relation is used where subordinate requires and the node
provides.

The "ready" relation uses the `ReadyUnitSuperInterface` which is available
in the default interface registry under `relation-subordinate-ready`.

## Contributing

Please see the [Juju SDK docs](https://juju.is/docs/sdk) for guidelines
on enhancements to this charm following best practice guidelines, and
`CONTRIBUTING.md` for developer guidance.
