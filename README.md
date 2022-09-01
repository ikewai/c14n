## ikewai/c14n: Science Workflow Containerization

**A collection of container definitions and tools for portable, composable, and reproducible science workflows.**

Designed for storage and spin-up-time efficiency, these containers are purpose-built for their respective tasks. The containers are built to run on Tapis' Abaco system, but may also be ran on standard docker configurations with the appropriate environment configuration.

### Folder Structure
* [`containers`](/containers): All of the containers in the containerization system.
	* [`core`](/containers/core): Essential container definitions.
        * [`task-base`](/containers/core/task-base): A fundamental, baseline container that serves as a starting point for new workflows.
    * [`shared`](/containers/shared): Containers that are used to support multiple workflows.
	    * [`rf-at-acquisition-daily`](/containers/shared/rf-at-acquisition-daily): Pulling data for use with the _rainfall_ and _airtemp_ workflows.
    * [`rainfall`](/containers/rainfall): The rainfall data aggregation, and mapping processes.
	    * [`preliminary`](/containers/rainfall/preliminary): Preliminary workflow.
			* [`base`](/containers/rainfall/preliminary/base): Programs and libraries used across the rainfall workflows.
		    * [`aggregation`](/containers/rainfall/preliminary/aggregation): Aggregation and mapping tasks.
		    
    * [`airtemp`](/containers/airtemp): The air temperature data aggregation, and mapping processes.
	    * [`preliminary`](/containers/airtemp/preliminary): Preliminary workflow.
			* [`base`](/containers/airtemp/preliminary/base): Programs and libraries used across the airtemp workflows.
		    * [`aggregation`](/containers/airtemp/preliminary/aggregation): Aggregation task. 
				* [`base`](/containers/airtemp/preliminary/base): Essentials for aggregating air temperature data.
				* [`daily`](/containers/airtemp/preliminary/aggregation/daily): Aggregation on the daily frequency.
		    * [`mapping`](/containers/airtemp/preliminary/mapping): Mapping tasks.
				* [`daily`](/containers/airtemp/preliminary/mapping/daily): Map generation on the daily frequency.
	* [`ingestion`](/containers/ingestion): The metadata and station value ingestion processes.
 * [`tools`](/tools): Scripts and data files to support building and tagging.
	 * [`build-tools`](/tools/build-tools): Scripts that aid in build-time tasks, such as downloading files and constructing directory paths.
	 * [`runtime-tools`](/tools/runtime-tools): Scripts that aid in run-time tasks, such as uploading workflow-generated files.
	 * [`tagging-tools`](/tools/tagging-tools): Scripts that handle provenance tasks such as making the container manifest (during build-time) and submitting execution info to the gateway (during run-time).

To build a container, run the following in the root of the repo:
`docker build -f ./[path]/Dockerfile -t {tag} .`

For example, to build the task-base container:
`docker build -f ./containers/core/task-base/Dockerfile -t ikewai/task-base .`