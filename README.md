## ikewai/c14n: Science Workflow Containerization

**A collection of container definitions for portable, composable, and reproducible science workflows.**

Designed for storage and spin-up-time efficiency, these containers are purpose-built for their respective tasks. The containers are built to run on Tapis' Abaco system, but may also be ran on standard docker configurations with the appropriate environment configuration.

### Folder Structure
* [`containers`](/containers): All of the containers in the containerization system.
	* [`core`](/containers/core): Essential container definitions.
        * [`task-base`](/containers/core/task-base): A fundamental, baseline container that serves as a starting point for new workflows.
    * [`shared`](/containers/shared): Containers that are used to support multiple workflows.
	    * [`rf-at-acquisition-daily`](/containers/shared/rf-at-acquisition-daily): Pulling data for use with the _rainfall_ and _airtemp_ workflows.
    * [`rainfall`](/containers/rainfall): The rainfall data aggregation, and mapping processes.
	    * [`preliminary`](/containers/rainfall/preliminary): Preliminary workflow.
		    * [`aggregation`](/containers/rainfall/preliminary/aggregation): Aggregation task.
		    * [`mapping-monthly`](/containers/rainfall/preliminary/mapping-monthly): Mapping task, on the monthly frequency.
    * [`airtemp`](/containers/airtemp): The air temperature data aggregation, and mapping processes.
	    * [`preliminary`](/containers/airtemp/preliminary): Preliminary workflow.
		    * [`aggregation`](/containers/airtemp/preliminary/aggregation): Aggregation task. 
		    * [`mapping-daily`](/containers/airtemp/preliminary/mapping-daily): Mapping task on the daily frequency.
 * [`tools`](/tools): Scripts and data files to support building and tagging.
	 * [`build-tools`](/tools/build-tools): Scripts that aid in build-time tasks, such as downloading files and constructing directory paths.
	 * [`runtime-tools`](/tools/runtime-tools): Scripts that aid in run-time tasks, such as uploading workflow-generated files.
	 * [`tagging-tools`](/tools/tagging-tools): Scripts that handle provenance tasks such as making the container manifest (during build-time) and submitting execution info to the gateway (during run-time).