# ISC23_tutorial

#Introduction to the eFlows4HPC software stack and HPC Workflows as a Service methodology

## ISC-HPC tutorial, Hamburg May 21st, 2023 

## Abstract 
The tutorial will give an overview of the eFlows4HPC software stack and of the HPC
Workflows as a Service (HPCWaaS) methodology. The eFlows4HPC project
(https://eflows4hpc.eu/) aims to widen access to HPC to newcomers and to simplify the
development, deployment and execution of complex workflows in HPC systems. It proposes
to simplify this process in two ways. From one side, the eFlows4HPC software stack aims to
provide the required functionalities to manage the workflow's lifecycle. On the other side, it
introduces the HPCWaaS concept, which leverages the software stack to widen access to
HPC systems. This service offering tries to bring the Function as a Service (FaaS) concept
to the HPC environments hiding the complexity of an HPC Workflow execution to end users.

The tutorial will be composed of two parts. First, it will present an overview of the project
software stack. Then, it will introduce how workflows are developed in the project, through
three different components: computational aspects (PyCOMPSs), data transfers (Data
Pipelines) and overall topology (TOSCA). The second part will be more practical, showing
how to generate specific containers that leverage the HPC systems features (hands-on
component), how to move data from repositories to the HPC systems, and how to deploy the
workflows with Alien4Cloud.

## Agenda
 
| Time | Session | Presenter |
| --- | --- | --- | 
| 09:00 – 09:15 | [Overview of eFlows4HPC project and tutorial agenda](slides/eFlows4HPC_ISC_tutorial_intro.pdf) | Rosa M Badia (BSC) |
| 09:15 - 09:35 | [Part 1.1: Integrating different computations in PyCOMPSs](slides/eFlows4HPC_ISC_tutorial_part1.1.pdf) | Rosa M Badia (BSC) |
| 09:35 – 10:05 | Part 1.2: HPC ready container images | Jorge Ejarque (BSC) |
| 10:05 - 10:35 | [Part 1.3: Data Pipelines and Data Logistics Service (DLS)](slides/eFlows4HPC_ISC_tutorial_part1.3.pdf) | Jedrzej Rybicki (JSC) |
| 10:35 - 10:55 | Part 1.4: TOSCA Orchestration and HPCWaaS |  Jorge Ejarque (BSC) |
| 10:55 – 11:00 | Conclusion of part 1 |  Rosa M Badia (BSC) |
| 11:00 - 11:30 |  Coffee break | | 
| 11:30 - 12:05 | Part 2.1: Hands-on session: How to build HPC Ready containers | Jorge Ejarque (BSC) |
| 12:05 - 12:30 | Part 2.2: Hands-on session: How to move data with the DLS  | Jedrzej Rybicki (JSC)|
| 12:30 - 12:45 | Part 2.3: Video demonstrating deployment with Allien4Cloud | |
| 12:45 - 13:00 | Tutorial conclusions  | all presenters |
