## Rainfall (Preliminary) Data Processing Containers

These containers handle the processes of aggregating, quality-controlling, and mapping rainfall data, which is originally collected by the [data acquisition containers](../../../containers/shared/acquisition).

Contents:
* [`base`](/base): OS Packages and Libraries necessary for running the R workflows.
* [`aggregation/base`](/aggregation/base): Last-step file acquisition and setup. Possibly unnecessary, may remove later.
* [`aggregation/daily`](/aggregation/daily): Daily aggregation and mapping.
* [`aggregation/monthly`](/aggregation/monthly): Monthly aggregation and mapping.
