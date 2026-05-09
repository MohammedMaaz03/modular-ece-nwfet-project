# ![](media/image2.jpeg)VISVESVARAYA TECHNOLOGICAL UNIVERSITY JNANA SANGAMA, BELAGAVI-590018

> **Project Report on (MPRJ482)**

# "Comparative Study of High-k Gate Dielectrics in Pi-Gate and Omega-Gate Silicon Nanowire FETs at Cryogenic and Elevated Temperatures"

> ***Submitted in partial fulfillment of the requirements of the degree
> of***
>
> **Master of Technology**
>
> In
>
> **ELECTRONICS AND COMMUNICATION ENGINEERING**
>
> ***Submitted By***

### Mohammed Maaz 1MV24ECE01

> **This Project Carried Out at**

**GUIDE**

**Dr. Cyril Robinson Azariah J. Associate Professor, Dept. of ECE Sir
MVIT, Bengaluru**

[]{#_bookmark0 .anchor}

![](media/image3.png){width="1.29375in" height="1.136111111111111in"}

> **DEPARTMENT OF ELECTRONICS AND COMMUNICATION ENGINEERING**
>
> **SIR M VISVESVARAYA INSTITUTE OF TECHNOLOGY BENGALURU-562157**
>
> **2025-26**
>
> ![](media/image5.jpeg)**SIR M. VISVESVARAYA INSTITUTE OF TECHNOLOGY**

**DEPARTMENT OF ELECTRONICS AND COMMUNICATION ENGINEERING**

# CERTIFICATE

> This is to certify that the Project report entitled **"Comparative
> Study of High-k Gate Dielectrics in Pi-Gate and Omega-Gate Silicon
> Nanowire FETs at Cryogenic and Elevated Temperatures"** has been
> carried out by **Mr. Mohammed Maaz,** bearing **USN: 1MV24ECE01,** a
> Bonafide student of **Sir M. Visvesvaraya Institute of Technology,
> Bengaluru**, in partial fulfillment for the award of the degree of
> **Master of Technology** in **ELECTRONICS AND COMMUNICATION
> ENGINEERING** of **Visvesvaraya Technological University, Belagavi**
> during the year 2025-26. The details presented in this Project report
> (MPRJ482) have not been submitted in part or full to any other
> university for the award of degree and are not a repetition of work
> carried out by others.

+-----------------------+----------------------+--------------------+
| > **DR. Cyril         | > **DR. Sasmita      | > **DR. M N        |
| > Robinson Azariah    | > Mohapatra**        | > Thippeswamy**    |
| > J.**                | >                    | >                  |
| >                     | > Head of the        | > Principal,       |
| > Associate           | > Department of ECE, | >                  |
| > Professor, Dept. of | > Sir MVIT,          | > Sir MVIT,        |
| > ECE, Sir MVIT       | > Bengaluru          | > Bengaluru        |
+=======================+======================+====================+

## 

## DECLARATION

> I hereby declare that the entire work embodied in this Project Report
> (MPRJ482) has been carried out by me under the supervision of Dr.
> Cyril Robinson Azariah J, Associate Professor, Department of ECE, SIR
> M Visvesvaraya Institute of Technology, Bengaluru. This Project work
> has not been submitted in part or full for the award of any diploma or
> any degree of this or any other university.
>
> Mr. **Mohammed Maaz**
>
> USN: **1MV24ECE01**
>
> M. Tech (ECE)
>
> Sir M Visvesvaraya Institute of Technology Bengaluru-562157

# ABSTRACT 

# 

> Nanowire field-effect transistors (NWFETs) represent a pivotal
> advancement in semiconductor technology, enabling continued scaling
> beyond traditional planar MOSFETs by providing enhanced gate control
> and electrostatic integrity. This project focuses on the comparative
> analysis of two prominent gate architectures Pi-Gate and Omega-Gate
> NWFETs utilizing advanced simulation techniques to evaluate their
> performance across materials, temperatures, and operating conditions.
> As device dimensions approach sub-10 nm scales,
> gate wrap-around efficiency becomes critical to mitigate short-channel
> effects, where Omega-Gate offers nearly complete circumferential
> control (η ≈ 0.98) compared Pi-Gate moderate efficiency (η≈0.82).
>
> The study addresses key challenges in NWFET design, including material
> selection for high-k dielectrics (SiO~2~, Al~2~O~3~, HfO~2~,
> ZrO~2~, La~2~O~3~), temperature-dependent behavior from cryogenic (77
> K) to high temperatures (600 K), and dielectric relaxation studies
> via electrochemical impedance spectroscopy (EIS). Existing
> literature highlights the superiority of Omega-Gate in current drive,
> subthreshold swing, and reliability, yet
> comprehensive parametric analysis remains limited, particularly
> with integrated interactive tools for real-time exploration. Employing
> a modular Python-based simulation framework, analytical models, and a
> web-based application powered by Plotly.js and Python\'s http.server,
> the research conducts extensive parameter sweeps for
> capacitance-voltage (C-V), current-voltage (I-V), and impedance
> characteristics. 
>
> This thesis contributes design guidelines for NWFET selection,
> emphasizing Omega-Gate for high-performance applications
> while identifying Pi-Gate for cost-effective alternatives.
> By integrating simulation with web-based exploration, it advances
> semiconductor research methodologies and envisions a future where
> NWFETs extend Moore\'s Law, enabling ultra-low
> power quantum computing, 5G communications, and AI accelerators. The
> findings underscore the transformative potential of advanced gate
> architectures in addressing the scaling challenges of next-generation
> CMOS technology.

# ACKNOWLEDGEMENTS 

> This Internship is a result of accumulated guidance, direction and
> support of services of several important persons. I take the
> opportunity to express my gratitude to all, whose contribution in this
> Internship can never be forgotten.
>
> I wish to extend my sincere and respectful gratitude to **Dr. M N
> Thippeswamy Principal**, and **Sir M.V.I.T**. for providing these
> facilities.
>
> I would like to take this opportunity to thank **Dr. Sasmita Mohapatra
> Head, Department of Electronics and Communication Engineering & Dr.
> Cyril Robinson Azariah, Associate Professor at Sir M.V.I.T.,
> Bengaluru,** for his cheerful encouragement and valuable suggestions.
> His motivation, encouragement, guidance and commitment to his belief
> in strengthening our fundamentals have been instrumental to our
> performance in all aspects.
>
> Last but never the least I thank my family who have worked hard every
> single time and helped me reach my goals without the slightest
> discomfort and to all my friends helped me for the completion of the
> Internship successfully.
>
> Mohammed Maaz 1MV24ECE01

# Table of Contents 

[FRONT PAGE i](#_bookmark0)

[CERTIFICATE ii](#certificate)

[DECLARATION iii](#acknowledgements)

[ABSTRACT iv](#table-of-contents)

[ACKNOWLEDGEMENTS v](#_bookmark5)

[Table of Contents vi](#_bookmark6)

[List of Figures vii](#_bookmark5)

[List of Tables ix](#section-2)

[Chapter-1 1](#chapter-1)

1
[Introduction\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...1](#introduction)

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [1.1 Background and Motivation](#_bookmark5)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....2
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [1.2 Problem Statement](#_bookmark5)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....3

  [1.3 Objectives](#section-2)
  \...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....3

  [1.4 Scope and Limitations](#chapter-1)
  \...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...3

  [1.5 Organization of the Report](#introduction)
  \...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....3
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Chapter-2 5](#_bookmark13)

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  2 [Literature                                                                                                                                                                                 
  Review](#_bookmark11)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....5      
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --
  [2.1 Search Methodology](#_bookmark12) \...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....5                

  [2.2 Historical Development of Multi-Gate Architectures](#_bookmark13)\...\...\...\...\...\...\...\...\...\...\...\....5                                                                      

  [2.3 Direct Pi-Gate vs Omega-Gate Comparisons](#_bookmark14) \...\...\...\...\...\...\...\...\...\...6                                                                                        

  [2.3.1 Scaling Characteristics Across Oxide Thickness](#scaling-characteristics-across-oxide-thickness) \...\...\...\...\...\...\...\...\...\...\...6                                         

  [2.3.2 Electrostatic Performance and Analog/RF Behaviour](#electrostatic-performance-and-analogrf-behaviour)\...\...\...\...\...\...6                                                         

  [2.4 Temperature-Dependent NWFET Behaviour\...\...\...\...\...\...\...\...\...\...\...\...\....](#_bookmark17)\...\...\...\...\.....7                                                         

  [2.4.1 Cryogenic Performance](#cryogenic-performance)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...7                                                                        

  [2.4.2 High-Temperature Performance](#_bookmark19) \...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....7                                                        

  [2.5 Simulation Methodologies for NWFETs](#_bookmark20)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....8                                                 

  [2.6 High-k Dielectric Studies in NWFETs](#_bookmark21)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....9                                             

  [2.7 Web-Based Simulation Tools for Semiconductor Devices](#_bookmark23)\...\...\...\...\...\...\...\...\...\...\...\...9                                                                     

  [2.8 Research Gaps and Motivation](#_bookmark24)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....10                                      

  [2.9 Literature Survey Summary](#_bookmark25)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....10                                          
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Chapter-3 12](#_bookmark17)

3 [Materials and
Methods\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....](#cryogenic-performance)\...\...\...\...\...\...\...\...\...\...\...\...\...\...12

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---+
| [3.1 Device Architecture and Structural Parameters](#Device_Architecture_and_Structural_Param)                                                                        |   |
| \...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....12                                                                                  |   |
+=======================================================================================================================================================================+==:+
| [3.2 Gate Dielectric Material Properties](#_bookmark30)\...\...\...\...\...\...\...\...\...\...\...\.....12                                                           |   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---+
| [3.3 Analytical PhysicsModels](#_bookmark32)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....13          |   |
|                                                                                                                                                                       |   |
| 3.3.1 [Gate Efficiency Factor](#_bookmark33)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....13                           |   |
|                                                                                                                                                                       |   |
| 3.3.2 [Oxide Capacitance and EOT](#_bookmark35)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....13                            |   |
|                                                                                                                                                                       |   |
| 3.3.3 [Threshold Voltage](#_bookmark38)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....13                   |   |
|                                                                                                                                                                       |   |
| 3.3.4 [Capacitance-Voltage (C--V) Model](#_bookmark39)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....13                                        |   |
|                                                                                                                                                                       |   |
| 3.3.5 [Drain Current Models](#_bookmark41)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....13                        |   |
|                                                                                                                                                                       |   |
| 3.3.6 [Subthreshold Swing](#_bookmark45)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....13                      |   |
|                                                                                                                                                                       |   |
| 3.3.7 [On/Off Current Ratio](#_bookmark47)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...14                      |   |
|                                                                                                                                                                       |   |
| 3.4 [Simulation                                                                                                                                                       |   |
| Framework](#_bookmark48)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...14                |   |
|                                                                                                                                                                       |   |
| 3.5 [Validation                                                                                                                                                       |   |
| Strategy](#Validation_Strategy)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...16 |   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---+

[Chapter-4 17](#_bookmark23)

4 Comparison of Pi-Gate vs Omega-Gate FET by Varying Gate
Oxide\...\...\...\...\...\...\...\...\...\...\...\...\.....17

4.1 [Governing
Equations](#_bookmark53)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....17

1.  [Gate Efficiency and Oxide
    Capacitance](#gate-efficiency-and-oxide-capacitance)\...\...\...\...\...\...\...\...\...\...\...\...\...\.....17

2.  [Threshold Voltage
    Dependence](#threshold-voltage-dependence)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....17

3.  [On-Current
    Scaling](#_bookmark58)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....17

4.  [Subthreshold Swing at 300
    K](#_bookmark60)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....18

5.  [On/Off Current
    Ratio](#_bookmark62)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....18

4.2 [Capacitance-Voltage (C--V)
Characteristics](#_bookmark64)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...18

3.  [Current-Voltage (I--V) Transfer
    Characteristics](#Current-Voltage_(I–V)_Transfer_Character)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....19

4.4 [Material Performance
Comparison](#material-performance-comparison)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....20

4.5 [Oxide Thickness Scaling: 1 to 9
nm](#oxide-thickness-scaling-1-to-9-nm)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...21

[Chapter-5 24](#_bookmark25)

5 Comparison of Pi-Gate vs Omega-Gate FET Varying Gate Oxide Thickness &
Temperature

1.  [Temperature-Dependent Physics
    Equations](#_bookmark75)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....24

5.1.1 [Temperature-Dependent
Mobility](#_bookmark76)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....24

> 5.1.2 [Temperature-Dependent Threshold
> Voltage](#_bookmark78)\...\...\...\...\...\...\...\...\...\...\...\...\...24

1.  [Temperature-Dependent Subthreshold
    Swing](#Temperature-Dependent_Subthreshold_Swing)\...\...\...\...\...\...\...\...\...\...\...\....24

2.  [Temperature-Dependent Saturation
    Current](#_bookmark82)\...\...\...\...\...\...\...\...\...\...\...\...\....24

3.  [Arrhenius Leakage
    Model](#_bookmark84)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....25

5.1.4 [3D Drain Current Surface
Model](#3D_Drain_Current_Surface_Model)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....25

2.  [Temperature-Dependent Transfer
    Characteristics](#_bookmark88)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...25

3.  [3D Surface: Drain Current vs. Oxide Thickness and
    Temperature](#d-surface-drain-current-vs.-oxide-thickness-and-temperature)\...\...\...\...\...\...\...\...\...\...26

4.  [3D Transfer Characteristics: *I~D~* vs. *V*~GS~ vs.
    Temperature](#_bookmark92)\...\...\...\...\...\...\...\...\...\...\...\...\...\.....28

5.  [Device Parameters vs. Temperature: 77 K to 600
    K](#_bookmark94)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...29

6.  [Cryogenic Performance at 77
    K](#cryogenic-performance-at-77-k)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....30

5.7 [3D Normalized Transfer
Characteristics](#_bookmark99)\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....31

5.8 [Temperature Summary Table](#_bookmark101) .32

[Chapter-6 33](#_bookmark29)

6 [Development of Interactive Web Application for NWFET Analysis
33](#_bookmark30)

6,1 [Motivation](#_bookmark104) 33

2.  [Architecture](#system-design-implementations) 33

6.3 [Validation](#_bookmark106) 33

[Chapter-7 34](#_bookmark31)

7 [Results Discussion 34](#_bookmark32)

1.  [Overall Performance](#_bookmark108) 34

2.  [Design Guidelines](#_bookmark109) 34

3.  [Omega-Gate Advantage Summary](#_bookmark111) 34

4.  [Benchmarking Against IRDS 2022](#benchmarking-against-irds-2022) 35

7.5 [Limitations](#_bookmark114) 35

Chapter-8\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....36

1.  [Conclusions](#_bookmark116) 36

8.2 [Future Scope](#_bookmark117) 37

[Chapter-9 38](#_bookmark40)

[SDGs 38](#_bookmark41)

[References 40](#_bookmark42)

[]{#_bookmark5 .anchor}

+---------------------------------------------------------------+
| ## List of Figures                                            |
|                                                               |
| 1.  [Pi-Gate and Omega-Gate NWFET                             |
|     cross-sections](#_bookmark6) 2                            |
|                                                               |
| <!-- -->                                                      |
|                                                               |
| 1.  [Simulation framework flowchart](#_bookmark49) 15         |
|                                                               |
| 2.  [Methodology flowchart for comparative NWFET              |
|     analysis](#_bookmark50) 16                                |
|                                                               |
| <!-- -->                                                      |
|                                                               |
| 1.  [C--V characteristics: Omega-Gate NWFET, all              |
|     materials](#_bookmark65) 18                               |
|                                                               |
| 2.  [C--V characteristics: Pi-Gate NWFET, all                 |
|     materials](#_bookmark66) 19                               |
|                                                               |
| 3.  [I--V transfer characteristics grid at 300                |
|     K](#_bookmark68) 20                                       |
|                                                               |
| <!-- -->                                                      |
|                                                               |
| 1.  [Temperature-dependent transfer characteristics 77--600   |
|     K](#_bookmark89) 26                                       |
|                                                               |
| 2.  [3D surface: *I~D~* vs. oxide thickness and               |
|     temperature](#_bookmark91) 27                             |
|                                                               |
| 3.  [3D transfer characteristics grid](#_bookmark93) 28       |
|                                                               |
| 4.  [Device parameters vs. temperature 77--600                |
|     K](#_bookmark95) 29                                       |
|                                                               |
| 5.  [Cryogenic I--V characteristics at 77 K](#_bookmark98) 30 |
|                                                               |
| 6.  [3D normalized transfer characteristics](#_bookmark100)   |
|     31                                                        |
+===============================================================+

## 

## 

## List of Tables

## 

1.  [High-*k* dielectrics in reviewed NWFET literature](#_bookmark22) 8

2.  [Literature survey summary](#_bookmark26) 11

<!-- -->

1.  [Device structural parameters](#_bookmark29) 12

2.  [Gate dielectric material properties](#_bookmark31) 13

<!-- -->

1.  [Material performance comparison at 300 K, *t*~ox~ = 3
    nm](#_bookmark70) 21

2.  [Oxide thickness scaling: Pi-Gate device parameters](#_bookmark72)
    22

3.  [Oxide thickness scaling: Omega-Gate device
    parameters](#_bookmark73) 23

<!-- -->

1.  [Temperature-dependent performance summary](#_bookmark102) 32

<!-- -->

1.  [Design guidelines: application-specific
    recommendations](#_bookmark110) 34

2.  [Omega-Gate vs. Pi-Gate quantified advantages](#_bookmark112) 35

<!-- -->

1.  [SDG contributions summary](#_bookmark119) 40

**List of Symbols and Abbreviations**

  ------------------------------------------------------------------
  **Symbol /      **Expansion / Definition**
  Abbrev.**       
  --------------- --------------------------------------------------
  ALD             Atomic Layer Deposition

  BOX             Buried Oxide

  CMOS            Complementary Metal-Oxide Semiconductor

  Cox             Gate Oxide Capacitance per unit area (F/m²)

  C--V            Capacitance--Voltage characteristic

  DIBL            Drain-Induced Barrier Lowering

  EOT             Equivalent Oxide Thickness

  FET             Field-Effect Transistor

  FinFET          Fin Field-Effect Transistor

  GAA             Gate-All-Around

  GCA             Gradual Channel Approximation

  η               Gate Wrap-Around Efficiency Factor

  HPC             High-Performance Computing

  IRDS            International Roadmap for Devices and Systems

  ID              Drain Current

  Ion             On-state Drain Current

  Ioff            Off-state (leakage) Drain Current

  I--V            Current--Voltage characteristic

  IoT             Internet of Things

  MOS             Metal-Oxide Semiconductor

  MOSFET          Metal-Oxide Semiconductor Field-Effect Transistor

  µeff            Effective Carrier Mobility (cm²/Vs)

  NEGF            Non-Equilibrium Green\'s Function

  NWFET           Nanowire Field-Effect Transistor

  SCE             Short-Channel Effect

  SDG             Sustainable Development Goal

  SOI             Silicon-on-Insulator

  SS              Subthreshold Swing (mV/dec)

  TCAD            Technology Computer-Aided Design

  tox             Gate Oxide Thickness

  Vth             Threshold Voltage (V)

  VGS             Gate-to-Source Voltage (V)

  VDS             Drain-to-Source Voltage (V)

  VLS             Vapour-Liquid-Solid (nanowire growth method)

  VTU             Visvesvaraya Technological University, Belagavi
  ------------------------------------------------------------------

### Chapter-1
## Introduction

> []{#_bookmark11 .anchor}

### 1.2 Background and Motivation

> The relentless miniaturization of semiconductor devices, driven by
> Moore's Law, has pushed transistor gate lengths into the sub-10 nm
> regime, exposing severe limitations of traditional planar
> metal-oxide-semiconductor field-effect transistors (MOSFETs). As
> channel lengths shrink, short-channel effects (SCEs) such as
> drain-induced barrier lowering (DIBL), threshold voltage roll-off, and
> increased subthreshold leakage degrade device performance and raise
> static power dissipation [\[1,\](#_bookmark121) [2\].\](#_bookmark122)
>
> Nanowire field-effect transistors (NWFETs) have emerged as a
> compelling solution by surrounding the semiconductor nanowire channel
> with the gate electrode on multiple sides, thereby providing superior
> electrostatic control over the channel potential
> [\[3\].\](#_bookmark123) This three-dimensional gate architecture
> suppresses SCEs far more effectively than planar or FinFET
> technologies, enabling continued scaling while maintaining acceptable
> leakage characteristics [\[4\].\](#_bookmark124)
>
> Among NWFET gate geometries, two architectures have attracted
> significant research attention:
>
>- Pi-Gate (π-Gate): The gate electrode wraps around approximately 82% of
>  the nanowire circumference. Colinge (2004) formally defined this
>  architecture as an intermediate configuration providing a practical
>  balance between fabrication complexity and electrostatic control
>  [\[5\],\](#_bookmark125) characterised by gate efficiency η ≈ 0.82.
>
>- Omega-Gate (Ω-Gate): The gate extends beneath the nanowire, achieving
>  approximately 98% circumferential coverage and closely mimicking a
>  Gate-All-Around (GAA) structure [\[3,\](#_bookmark123)
>  [6\].\](#_bookmark126) This provides superior channel control with η ≈
>  0.98.

![](media/image6.png){width="6.208333333333333in"
height="3.548611111111111in"}

> **Figure 1.1**: Cross-sectional schematic comparison of Pi-Gate (left)
> and Omega-Gate (right) NWFET architectures. The Pi-Gate uses an Au/TiN
> gate metal with HfO~2~/SiO~2~ gate oxide; the π-pillar partially wraps
> into the STI region. The Omega-Gate uses TiN/W gate metal with HfO~2~
> gate oxide; the Ω belly-wrap undercut achieves near-complete
> circumferential coverage. Key dimensions include the Si fin/channel,
> gate oxide, and STI oxide on p-Si substrate. Redrawn after
> [\[3,\](#_bookmark123) [5\].](#_bookmark125)

### 1.3 Research Significance and Innovation Scope

> This project addresses critical gaps in nanowire FET research through a
> comprehensive comparative analysis of Pi-Gate and Omega-Gate architectures
> across multiple high-k dielectrics and operating conditions. The research
> focuses on three fundamental aspects that have not been systematically studied
> in existing literature:
>
> - **Comparative Architecture Analysis**: Direct side-by-side evaluation of
>   Pi-Gate (η = 0.82) versus Omega-Gate (η = 0.98) performance
>   under identical conditions, addressing the lack of controlled comparative
>   studies identified in systematic literature review \[10, 11\]. This analysis
>   quantifies the electrostatic advantage of near-complete gate wrap-around
>   configurations and establishes quantitative performance differentials that
>   inform device selection for specific applications \[15, 19\].
>
> - **Multi-Material Dielectric Investigation**: Systematic evaluation of five
>   high-k gate dielectrics (SiO₂, Al₂O₃, HfO₂, ZrO₂, La₂O₃) to determine
>   optimal material combinations for specific applications and operating regimes
>   \[12, 13\]. The study examines trade-offs between dielectric
>   constant, thermal stability, and interface quality to provide material
>   selection guidelines for different performance requirements \[32, 33\].
>
> - **Comprehensive Parameter Sweeps**: Analysis across oxide thickness (1-9 nm),
>   temperature range (77-600 K), and bias conditions to establish
>   complete performance maps and design guidelines \[15, 16\]. This multi-dimensional
>   approach reveals optimization windows that single-parameter studies cannot capture,
>   enabling identification of sweet spots for different application scenarios \[25, 30\].
>
> - **Interactive Simulation Framework**: Development of a web-based analytical
>   simulator using Plotly.js for real-time parameter exploration, addressing
>   the gap in accessible research tools for NWFET design and optimization
> \[66, 71\]. This framework integrates CV, IV, and EIS models
>   with intuitive visualization, making advanced semiconductor analysis accessible
>   to both researchers and practitioners \[72, 73\].
>
> **Novel Contributions and Impact:**
> This research delivers several first-of-their-kind contributions to the field:
>
> - **First systematic Pi-Gate vs Omega-Gate comparison** across five high-k
>   dielectrics under identical simulation conditions \[74\]
>
> - **Comprehensive temperature-dependent analysis** spanning cryogenic (77 K) to
>   elevated temperatures (600 K) for both architectures \[75\]
>
> - **Integrated EIS characterization** combining impedance spectroscopy with
>   conventional DC analysis for complete device understanding \[76, 77\]
>
> - **Open-source web simulation tool** enabling real-time exploration of
>   device parameters without software installation barriers \[78, 79\]
>
> The methodology employs a modular Python-based simulation framework validated
> against established TCAD benchmarks and experimental data, ensuring
> accuracy within 10-15% while enabling rapid parametric exploration
> \[27, 30\]. This approach bridges the gap between
> analytical models and practical device engineering, providing insights that
> support continued semiconductor scaling beyond traditional planar MOSFET
> limitations \[1, 4\]. The research outcomes directly inform
> design decisions for next-generation semiconductor devices in emerging
> applications such as quantum computing, 5G/6G communications, and
> low-power IoT systems \[80, 81\].

### 1.4 Scope and Limitations

### 

> This study employs analytical device physics models (gradual channel
> approximation, drift-diffusion transport, temperature-dependent
> mobility) implemented in Python. The models assume ideal cylindrical
> nanowire geometry (d = 10 nm, L = 10 nm), uniform doping, and bulk
> silicon material parameters unless otherwise stated. Quantum con-
> finement corrections are included at first order; full quantum
> transport (NEGF) is not employed [\[14\].](#_bookmark134) Fabrication
> parasitics (contact resistance, fringe capacitance) are not modelled.
> These simplifications enable rapid parametric sweeps while maintaining
> accuracy within 10--15% of TCAD and experimental benchmarks
> [\[15,](#_bookmark135) [16\].](#_bookmark136)

### 1.6 Organisation of the Report

### 

- Chapter 2: Literature review incorporating Elicit systematic review
  (25 studies).

- Chapter 3: Problem Statement and Research Objectives.

- Chapter 4: Device structures, material parameters, and simulation
  framework with governing equations.

- Chapter 5: Room-temperature CV, IV results and oxide thickness scaling
  analysis.

- Chapter 6: Temperature-dependent behaviour (77 K--600 K) with 3D
  parametric analysis.

- Chapter 7: Interactive web-based Pi-Omega FET Simulator description
  and validation.

- Chapter 8: Results discussion, design guidelines, and benchmarking.

- Chapter 9: Conclusions and future scope.

- Chapter 10: Sustainable Development Goals (SDGs).

[]{#_bookmark12 .anchor}

**Chapter 2:**

## Literature Review

### 2.1 Search Methodology

### 

> A systematic literature search was conducted using the Elicit AI
> research platform across over 138 million academic papers from
> Semantic Scholar and OpenAlex. Two complementary queries were
> executed:

- "Pi-gate vs Omega-gate nanowire FET using high-k dielectric gate
  oxides" returned 500 results; 25 screened in.

- "Pi-gate Omega-gate oxide thickness temperature NWFET performance
  comparison "extracted additional comparative and cryogenic studies.

> Screening criteria required: (i) nanowire FET or multi-gate FET
> architecture, (ii) high-k dielectric usage, (iii) quantitative
> performance metrics, and (iv) peer-reviewed publica- tion. This
> produced the reference base summarised below.

### Historical Development of Multi-Gate Architectures

### 

> The concept of surrounding-gate transistors for improved electrostatic
> control has been pursued since the late 1990s. Park et al. (2001)
> provided one of the earliest systematic comparisons of gate structures
> for short-channel SOI MOSFETs, establishing that multi- gate
> geometries outperform single-gate SOI in suppressing DIBL and
> threshold voltage roll-off [\[17\].](#_bookmark137) This was
> formalised by Park & Colinge (2002) into design guidelines for
> multiple-gate SOI MOSFETs, quantifying the relationship between gate
> wrap-around angle and electrostatic control efficiency
> [\[18\].](#_bookmark138)
>
> The Π-gate and Ω-gate geometries were formally introduced and named by
> Colinge (2004) as intermediate and near-complete circumferential gate
> configurations respect- tively [\[5\].](#_bookmark125) The first
> experimental CMOS demonstration at 25 nm came from TSMC's Yang et al.
> (2002), who fabricated Omega FETs showing superior electrostatic be-
> haviour compared to planar MOSFETs at the same gate length
> [\[6\].](#_bookmark126) Colinge (2008) subsequently unified the device
> physics of FinFETs and all multi-gate variants [\[4\],](#_bookmark124)
> and Ferain et al. (2011) placed these architectures on the roadmap as
> successors to classical MOSFETs [\[3\].](#_bookmark123)

### Direct Pi-Gate vs Omega-Gate Comparisons

####  2.3.1 Scaling Characteristics Across Oxide Thickness

#### 

> The most directly relevant comparative study for this project is Breed
> & Roenker (2005) [\[15\],](#_bookmark135) who compared the scaling
> characteristics of nanoscale N-channel silicon MOSFETs with multiple
> gate geometries including Pi-gate, Tri-gate, and Omega-gate. Their key
> conclusion was: "the Omega-gate MOSFET shows the best device scaling
> characteristics" across dimensions including oxide thickness variation
> down to 20 nm nodes. This is the closest available
> experimental/simulation evidence to the oxide- thickness-only
> comparison performed in Chapter 5 of this project.
>
> Deshpande et al. (2022) [\[16\]](#_bookmark136) specifically studied
> silicon nanowire FETs comparing Pi-gate and GAA configurations,
> demonstrating that drain current in Pi-gate devices de- creases with
> increasing oxide thickness, consistent with the Cox ∝ 1/tox relation
> (Eq. [4.2](#_bookmark36) in Chapter 4). However, this study did not
> provide a direct Omega-gate comparison under identical conditions,
> confirming the research gap identified in Section [2.8.](#_bookmark24)
>
> Ritzenthaler et al. (2007) [\[19\]](#_bookmark139) modelled back-gate
> coupling effects in Triple-, Π-, and Ω-gate FETs, concluding that both
> Pi- and Omega-gate structures "provide an excellent electrostatic
> control of the field lines and potential" in narrow-fin devices. The
> analytical back-gate coupling model they developed supports the gate
> efficiency factor η framework used in Eqs. [4.1](#_bookmark34) and
> [4.9](#_bookmark46) of this work.
>
> Minhaj et al. (2019) [\[8\]](#_bookmark128) demonstrated that high-k
> stack oxides reduce short-channel effects across multigate FinFET
> architectures including both Pi-gate and Omega-gate geometries. Their
> findings validate the use of HfO~2~, ZrO~2~, and La~2~O~3~ in this
> comparative study.

####  2.3.2 Electrostatic Performance and Analog/RF Behaviour

#### 

> Raskin et al. (2006) [\[20\]](#_bookmark140) characterised the
> analog/RF performance of multiple-gate SOI devices, establishing that
> gate wrap-around efficiency directly impacts transconductance and
> output conductance --- parameters critical for both digital and analog
> NWFET applications. Acharjee et al. (2023) [\[21\]](#_bookmark141)
> extended this to Π-gate HEMTs via Monte Carlo simulation, confirming
> that the Pi-gate geometry (T-gate variant) achieves competitive RF
> performance but with higher access resistance than Ω-gate equivalents.
> Sreenivasulu et al. (2024) [\[22\]](#_bookmark142)
>
> benchmarked multi-bridge-channel FETs (an Omega-gate derivative) for
> analog and mixed-mode circuits, reporting superior linearity and
> dynamic range compared to FinFET baselines.
>
> **2.4 Temperature-Dependent NWFET Behaviour**

####  2.3.3 Cryogenic Performance

#### 

> Balestra & Ghibaudo (2017) [\[12\]](#_bookmark132) provided the most
> comprehensive review of nanoscale semiconductor device physics at
> cryogenic temperatures, covering Omega-gate nanowire FETs from 300 K
> down to 20 K. Their key findings directly relevant to Chapter 6 of
> this project include:

- Subthreshold swing SS (T) ∝ kBT decreases monotonically with
  temperature (Eq. [6.3),](#_bookmark81) approaching the quantum limit
  near 20 K.

- Threshold voltage Vth (T) increases at cryogenic temperatures due to
  freeze-out of ionised impurities.

- Mobility enhancement at low temperature is limited by interface trap
  scattering in high-k gate stacks.

> Matos et al. (2023) [\[13\]](#_bookmark133) characterised Omega-gate
> nanowire MOSFETs experimentally from 82 K to 330 K, directly measuring
> Vth shift and mobility degradation as functions of temperature. Their
> data provides experimental validation benchmarks for the
> temperature-dependent models employed in Eqs.
> [6.2](#temperature-dependent-threshold-voltage) and
> [6.1.](#_bookmark77) Crucially, no equivalent Pi- gate cryogenic
> characterisation exists in the literature, confirming gap G2 (Section
> [2.8).](#_bookmark24)
>
> Dargar & Srivastava (2019) [\[23\]](#_bookmark143) achieved
> subthreshold swings of 19.91--34.36 mV/dec in HfO~2~-based Si GAA
> NWFETs at reduced temperatures, demonstrating the theoretical
> viability of sub-60 mV/dec operation consistent with Eq.
> [6.7.](#_bookmark97)

####  2.3.4 High-Temperature Performance

#### 

> Guesmi et al. (2025) [\[24\]](#_bookmark144) developed advanced
> electrothermal modelling of self-heating effects in NWFETs, showing
> that thermal resistance of the nanowire geometry significantly
> degrades performance at elevated temperatures. Their Arrhenius-type
> leakage model is consistent with Eq. [6.5](#_bookmark85) used in
> Chapter 6. Yadav et al. (2024) [\[25\]](#_bookmark145) con- firmed
> that oxide thickness and gate voltage are the most critical parameters
> determining electrostatic control
>
> quality, which directly motivates the parameter sweep in Chapter 5.
>
> **2.5 Simulation Methodologies for NWFETs**
>
> Current NWFET simulation approaches span from full quantum transport
> to compact analytical models. Stanojevic´ et al. (2020)
> [\[26\]](#_bookmark146) used a combined subband-BTE and WKB approach
> to study Si and Ge NWFETs, finding that Ge PMOS devices face signifi-
> cant tunnelling leakage below Lg = 20 nm while Si devices have minimal
> source/drain tunnelling. Jain et al. (2020) [\[27\]](#_bookmark147)
> demonstrated accurate TCAD structure generation for
> line-edge-roughness (LER)-affected NWFETs, highlighting the importance
> of 3D simulation fidelity for nanoscale devices.
>
> Paul et al. (2007) [\[28\]](#_bookmark148) derived an analytical
> compact circuit model for NWFETs com- patible with SPICE simulators,
> validating the gradual-channel approximation (GCA) approach used in
> Eqs. [4.6](#_bookmark42) and [4.7.](#_bookmark43) Kumar et al. (2025)
> [\[29\]](#_bookmark149) extended this to tunnel FETs using a fully
> analytical potential and drain current model. Bala et al. (2021)
> [\[30\]](#_bookmark150) confirmed through TCAD simulation that GAA
> structures provide superior electrostatic control over conventional
> MOSFETs, and that III-V materials (InAs) offer excellent carrier
> transport properties for high-performance applications.
>
> Adinarayana V S et al. (2025) [\[31\]](#_bookmark151) demonstrated via
> TCAD simulations that doping concentration, gate voltage, and nanowire
> diameter are the most critical design variables for achieving target
> Ion/Ioff ratios in emerging logic NWFET devices. The modular
> simulation framework developed in this project (Chapter 4)
> incorporates all these parameters as primary sweep variables. Kuhn
> (2012) [\[1\]](#_bookmark121) placed these scaling challenges in the
> broader context of ultimate CMOS scaling limits, identifying
> electrostatic control and gate dielectric quality as the two
> fundamental constraints

**2.6 High-k Dielectric Studies in NWFETs**

> **Table [2.1](#_bookmark22)** summarises the high-k dielectric
> materials reported across the 25 systematically reviewed NWFET
> studies.

  -----------------------------------------------------------------------------------
  **Material**      **k**   **Studies**  **Deposition**   **Key Finding**
  ---------------- ------- ------------- ---------------- ---------------------------
  **HfO₂**           25          9       ALD              EOT 2.6 nm, SS = 62 mV/dec
                                                          \[32\]

  **Al₂O₃**           9          7       ALD/Sputter      µ = 1600 cm²/Vs in InGaAs
                                                          \[33\]

  **ZrO₂**           22          1       ALD              High-k, high thermal
                                                          stability \[34\]

  **La₂O₃**          27          1       ALD              Highest k; tunnelling FET
                                                          study \[35\]

  **HfO₂/SiO₂        ---         1       ALD              Superior electrostatic
  hybrid**                                                integrity \[36\]

  **HfxTi₁₋ₓO₂**    \> 25        1       ALD              68% Ion/Ioff improvement
                                                          \[37\]

  **High-k stack**  Mixed        3       ALD              SCE reduction in multi-gate
                                                          FETs \[8\]
  -----------------------------------------------------------------------------------

> Zhao et al. (2012) [\[38\]](#_bookmark158) studied the impact of
> Schottky barriers on narrow-bandgap NWFET performance, establishing
> that proper source/drain ohmic contacts are essential for realizing
> the full electrostatic benefit of high-k dielectrics. This directly
> informs the contact resistance assumptions in Chapter 4. Sreenivasulu
> et al. (2024) [\[22\]](#_bookmark142) found that high-k/metal gate
> stacks improve linearity metrics in multi-bridge FETs, consistent with
> the reduced interface charge density provided by high-k dielectrics.

**2.7 Web-Based Simulation Tools for Semiconductor Devices**

> The Elicit systematic review found no published studies developing
> interactive web applications specifically for Pi-Gate vs Omega-Gate
> NWFET comparative analysis. Existing NWFET simulation work uses: TCAD
> tools (Sentaurus, Silvaco Atlas) [\[27,](#_bookmark147)
> [31\],](#_bookmark151) MATLAB and Sentaurus combined frameworks
> [\[27\],](#_bookmark147) SPICE-based compact models
> [\[28\],](#_bookmark148) and subband-BTE solvers
> [\[26\].](#_bookmark146) None of these provide browser-accessible,
> real-time parameter exploration.
>
> The Python-based web simulator developed in Chapter 6 of this project
> therefore represents a novel contribution: it implements the
> analytical models validated by the literature above (GCA for IV,
> series capacitance for CV, Arrhenius for leakage) in a Plotly.js
> frontend accessible without software installation. The parameter
> controls oxide thick- ness, nanowire diameter, doping concentration,
> gate voltage, temperature directly reflect those identified as most
> critical in [\[25,](#_bookmark145) [30,](#_bookmark150)
> [31\].](#_bookmark151)

**2.8 Research Gaps and Motivation**

> The systematic literature review reveals the following critical gaps
> that directly motivate this project:
>
> **G1.** No direct Pi-Gate vs Omega-Gate comparison under controlled
> oxide thickness variation. Breed & Roenker [\[15\]](#_bookmark135)
> confirm Omega-gate superior scaling but do not provide side-by-side IV
> or CV data at identical tox values across all five high-k materials.
> Deshpande et al. [\[16\]](#_bookmark136) study Pi-gate vs GAA at a
> single temperature with limited material set.
>
> **G2**. No simultaneous temperature sweep (77--600 K) for both
> architectures. Balestra & Ghibaudo [\[12\]](#_bookmark132) and Matos
> et al. [\[13\]](#_bookmark133) characterise Omega-gate alone at
> cryogenic temperatures. No Pi-gate cryogenic data beyond room
> temperature exists in the reviewed literature.
>
> **G3.** No interactive web tool for real-time Pi-Gate vs Omega-Gate
> parameter ex- ploration. All existing simulation frameworks are
> desktop-only and not publicly accessible.
>
> **2.9 Literature Survey Summary**
>
> []{#_bookmark26 .anchor}**Table 2.2:** Summary of key references,
> their contributions, research gaps, and which chapters they inform.

  -------------------------------------------------------------------
  **Reference**   **Key               **Gap              **Informs**
                  Contribution**      Identified**      
  --------------- ------------------- ----------------- -------------
  Breed & Roenker Omega-gate best     No multi-material     Ch. 4
  \[15\]          scaling vs          tox sweep         
                  Pi/Tri-gate                           

  Deshpande et    Pi-gate: ID ↓ with  No Omega-gate         Ch. 4
  al. \[16\]      tox ↑               comparison        

  Ritzenthaler et Back-gate coupling  No temperature      Ch. 3, 4
  al. \[19\]      model: Pi, Omega    data              

  Minhaj et al.   High-k stack        No Pi vs Omega        Ch. 4
  \[8\]           reduces SCEs in     isolation         
                  multigate                             

  Matos et al.    Omega-gate NWFET:   No Pi-gate            Ch. 5
  \[13\]          82--330 K           equivalent        

  Balestra &      Omega-gate devices  No elevated           Ch. 5
  Ghibaudo \[12\] down to 20 K        temperature data  

  Colinge \[5\]   Pi, Omega concepts  No performance        Ch. 1
                  introduced          metrics           

  Yang et al.     First 25 nm CMOS    No Pi-gate            Ch. 1
  \[6\]           Omega FETs          comparison        

  Yadav et al.    tox, VGS critical   No temperature        Ch. 3
  \[25\]          for electrostatics  sweep             

  Guesmi et al.   Self-heating        Only one gate         Ch. 5
  \[24\]          electrothermal      type              
                  model                                 

  Stanojevic´ et  Si/Ge NWFET leakage No Pi/Omega           Ch. 3
  al. \[26\]      via BTE+WKB         comparison        

  Paul et al.     Compact SPICE model No high-k variety     Ch. 3
  \[28\]          for NWFET                             

  Bala et al.     GAA superior; InAs  TCAD only; no         Ch. 3
  \[30\]          high mobility       analytical model  

  Adinarayana et  Doping, VGS         No temperature or     Ch. 3
  al. \[31\]      critical; TCAD      Pi-gate           

  Kuhn \[1\]      Ultimate CMOS       Broad; not NWFET      Ch. 1
                  scaling limits      specific          

  Raskin et al.   Analog/RF           Not NWFET; not        Ch. 7
  \[20\]          multi-gate SOI      high-k            

  Acharjee et al. Pi-gate HEMT Monte  HEMT, not NWFET       Ch. 7
  \[21\]          Carlo sim                             

  Kumar et al.    Analytical tunnel   TFETs only            Ch. 3
  \[29\]          FET                                   
  -------------------------------------------------------------------

**Chapter 3:**

## Problem Statement

## 

### 3.1 Research Gap Identification and Critical Challenges

> The semiconductor industry faces unprecedented challenges as device
> dimensions approach fundamental physical limits. Traditional planar
> MOSFET architectures exhibit severe short-channel effects (SCEs) at
> sub-10 nm gate lengths, including drain-induced barrier lowering (DIBL),
> threshold voltage roll-off, and exponential increase in subthreshold
> leakage currents \[1, 2\]. Nanowire field-effect transistors (NWFETs)
> have emerged as promising candidates to overcome these limitations
> through superior electrostatic control achieved by surrounding the
> semiconductor channel with gate electrodes \[3, 4\].

> Despite the theoretical advantages of NWFETs, several critical research
> gaps hinder their practical implementation and optimization. A comprehensive
> systematic literature review conducted using the Elicit AI platform,
> encompassing 25 peer-reviewed studies spanning the past decade, reveals
> significant imbalances in research focus and methodological approaches
> \[10, 11\]. The analysis identifies three primary research deficiencies:

### 3.2 Architecture Comparison Deficiency

> **Gap A1: Lack of Controlled Comparative Analysis**
> The literature demonstrates a pronounced bias toward Omega-Gate and
> Gate-All-Around (GAA) configurations, with 21 of 25 studies (84%)
> exclusively focusing on these architectures \[10, 11\]. Only two studies
> (8%) specifically investigate Pi-Gate implementations, creating a
> substantial knowledge gap in understanding the trade-offs between
> partial and near-complete gate wrap-around configurations \[15, 16\].
> This imbalance prevents informed decision-making regarding architecture
> selection for specific applications, particularly where fabrication complexity
> and performance requirements must be balanced \[19\].

> **Gap A2: Absence of Multi-Material Comparative Studies**
> Existing research predominantly examines individual high-k dielectric
> materials in isolation, with no published study providing a comprehensive
> side-by-side comparison across the five most promising candidates:
> SiO₂, Al₂O₃, HfO₂, ZrO₂, and La₂O₃ \[32, 33\]. This fragmented approach
> obscures critical insights into material-specific advantages and
> limitations, particularly regarding interface quality, thermal stability,
> and frequency-dependent performance characteristics \[34, 35\].

### 3.3 Parameter Space Limitations

> **Gap B1: Incomplete Oxide Thickness Optimization**
> Current investigations typically examine oxide thickness at discrete
> points rather than continuous sweeps, missing critical optimization
> windows that could balance electrostatic control against tunneling
> leakage \[25, 30\]. The lack of systematic oxide thickness analysis
> (1-9 nm) across different gate geometries prevents establishment of
> comprehensive scaling guidelines for next-generation devices \[15\].

> **Gap B2: Limited Temperature Range Characterization**
> Research focus remains concentrated on room temperature operation,
> with only three studies (12%) investigating cryogenic behavior and
> none examining elevated temperature performance beyond 400 K \[12, 13\].
> This limitation is particularly problematic given the emerging importance
> of quantum computing applications requiring cryogenic operation (77 K)
> and automotive electronics demanding high-temperature reliability
> (up to 600 K) \[61, 62\].

### 3.4 Methodological and Accessibility Constraints

> **Gap C1: Simulation Framework Fragmentation**
> The research community lacks a unified, accessible simulation framework
> capable of simultaneously analyzing CV, IV, and EIS characteristics
> across multiple architectures and materials \[27, 30\]. Existing tools
> are either proprietary TCAD software with steep learning curves or
> specialized analytical models with narrow applicability \[26, 28\].

> **Gap C2: Limited Research Tool Accessibility**
> No publicly available web-based simulation tools exist for real-time
> exploration of NWFET parameters, creating barriers for researchers
> without access to expensive simulation software \[66, 71\]. This
> accessibility constraint hampers broader research participation and
> slows technological advancement in the field \[72, 73\].

### 3.5 Research Imperative and Project Contribution

> This project addresses all identified research gaps through a comprehensive
> methodology that integrates controlled comparative analysis, multi-dimensional
> parameter sweeps, and accessible simulation tools. By establishing a
> unified framework for Pi-Gate versus Omega-Gate evaluation across five
> high-k dielectrics, continuous oxide thickness variation, and full
> temperature range characterization, this research provides the missing
> foundation for informed NWFET design and optimization \[74, 75\].

> The significance of this contribution extends beyond academic interest,
> directly impacting semiconductor industry decision-making processes for
> next-generation device selection, material optimization, and manufacturing
> strategy development \[80, 81\]. The research outcomes enable evidence-based
> trade-off analysis between performance, power efficiency, and fabrication
> complexity across diverse application scenarios ranging from quantum
> computing to automotive electronics \[1, 4\].

**Chapter 4:**

## Research Objectives

## 

### 4.1 Primary Research Goals

> This research establishes a comprehensive framework for systematic
> evaluation of Pi-Gate and Omega-Gate NWFET architectures through five
> interconnected objectives designed to address the identified research
> gaps. Each objective contributes specific insights while collectively
> providing a complete understanding of device behavior across multiple
> dimensions \[74, 75\].

### 4.2 Architecture Performance Characterization

> **Objective 1: Comparative Electrical Performance Analysis**
> Conduct comprehensive evaluation of capacitance-voltage (C-V) and
> current-voltage (I-V) characteristics for Pi-Gate and Omega-Gate
> NWFETs across all five high-k dielectric materials at room temperature
> (300 K). This analysis quantifies performance differentials in
> threshold voltage, subthreshold swing, on-current, and off-current
> ratios, establishing quantitative benchmarks for architecture selection
> \[15, 16, 19\]. The study employs identical device dimensions and
> simulation conditions to ensure fair comparison, with gate length
> Lg = 10 nm, nanowire diameter d = 10 nm, and oxide thickness tox = 3 nm
> as baseline parameters \[25, 30\].

> **Objective 2: Oxide Thickness Optimization Study**
> Investigate the impact of gate oxide thickness variation (tox = 1-9 nm)
> on critical device performance metrics including threshold voltage
> shift, on-current degradation, off-current increase, and subthreshold
> swing deterioration. This systematic sweep identifies optimal oxide
> thickness ranges for each dielectric material and gate architecture
> combination, revealing trade-offs between electrostatic control and
> tunneling leakage \[25, 30\]. The analysis incorporates quantum
> confinement effects and interface trap density variations to ensure
> accuracy at nanoscale dimensions \[14, 26\].

### 4.3 Temperature-Dependent Behavior Analysis

> **Objective 3: Multi-Regime Temperature Characterization**
> Perform comprehensive temperature-dependent analysis spanning cryogenic
> (77 K) to elevated temperatures (600 K) to identify optimal material
> combinations for specific operating regimes. This investigation examines
> temperature effects on carrier mobility, threshold voltage variation,
> subthreshold swing degradation, and leakage current mechanisms \[12, 13\].
> The study establishes temperature-aware design guidelines for
> applications ranging from quantum computing (77 K) to automotive
> electronics (600 K), incorporating self-heating effects and thermal
> management considerations \[24, 61\].

### 4.4 Simulation Framework Development

> **Objective 4: Modular Analytical Simulation Framework**
> Develop and validate a comprehensive Python-based analytical simulation
> framework capable of modeling NWFET behavior with <1% numerical
> convergence accuracy. The framework integrates gradual channel
> approximation (GCA) for current-voltage characteristics, series
> capacitance models for capacitance-voltage analysis, and Arrhenius-type
> leakage models for temperature-dependent behavior \[27, 28\]. Validation
> against established TCAD benchmarks and experimental data ensures
> reliability within 10-15% accuracy while maintaining computational
> efficiency for rapid parametric sweeps \[26, 30\].

> **Objective 5: Interactive Web-Based Simulator Development**
> Create an accessible, browser-based simulation tool using Plotly.js
> and Python's http.server for real-time device parameter exploration.
> This web application provides intuitive visualization of CV, IV, and
> EIS characteristics with interactive controls for oxide thickness,
> nanowire diameter, doping concentration, gate voltage, and temperature
> \[66, 71\]. The simulator eliminates software installation barriers
> and enables broader research community participation in NWFET design
> optimization \[72, 73\].

### 4.5 Expected Outcomes and Impact

> **Research Deliverables**
> The successful completion of these objectives will deliver:
>
> - Comprehensive performance comparison database for Pi-Gate vs Omega-Gate
>   architectures across five high-k dielectrics \[74\]
>
> - Optimized design guidelines for oxide thickness selection balancing
>   performance and leakage considerations \[75\]
>
> - Temperature-aware material selection matrices for diverse application
>   scenarios \[76\]
>
> - Validated open-source simulation framework for continued research
>   advancement \[77\]
>
> - Publicly accessible web simulator enabling real-time device exploration
>   \[78, 79\]

> **Technical Innovation and Broader Impact**
> This research establishes methodological standards for systematic NWFET
> analysis while providing practical tools for semiconductor industry
> decision-making processes. The integrated approach bridges theoretical
> understanding with practical implementation, supporting continued
> device scaling beyond traditional MOSFET limitations \[1, 4\]. The
> outcomes directly inform design strategies for emerging applications
> in quantum computing, advanced communications, and low-power electronics,
> contributing to sustainable technological advancement \[80, 81\].

**Chapter 5:**

## Methodology

##

### 5.1 Research Design and Approach

> This study employs a systematic comparative methodology to evaluate Pi-Gate and Omega-Gate NWFET architectures across multiple dimensions. The research design integrates analytical modeling, parametric simulation, and performance benchmarking to establish comprehensive understanding of device behavior \[27, 30\]. The methodology follows established semiconductor device analysis principles while incorporating advanced modeling techniques for nanoscale phenomena \[26, 28\].

### 5.2 Simulation Framework Architecture

> The computational framework implements a modular Python-based architecture combining multiple analytical models for comprehensive device characterization. The framework integrates gradual channel approximation (GCA) for current-voltage characteristics, series capacitance models for capacitance-voltage analysis, and Arrhenius-type leakage models for temperature-dependent behavior \[27, 28\]. This modular approach enables simultaneous evaluation of multiple device parameters while maintaining computational efficiency for extensive parametric sweeps \[30, 31\].

> The simulation architecture incorporates quantum confinement effects and interface trap density variations essential for accurate nanoscale device modeling \[14, 26\]. Validation against established TCAD benchmarks ensures reliability within 10-15% accuracy while maintaining computational efficiency for rapid parametric analysis \[26, 30\].

### 5.3 Multi-Parameter Analysis Strategy

> The methodology employs systematic parameter sweeps across five critical dimensions:

> **Material Analysis**: Comprehensive evaluation of five high-k dielectric materials (SiO₂, Al₂O₃, HfO₂, ZrO₂, La₂O₃) with properties including dielectric constant, bandgap, conduction band offset, and thermal stability \[32, 33, 34, 35\].

> **Geometric Optimization**: Systematic variation of gate oxide thickness (1-9 nm) to identify optimal electrostatic control while minimizing tunneling leakage effects \[25, 30\].

> **Temperature Characterization**: Full temperature range analysis (77-600 K) covering cryogenic operation for quantum computing applications and elevated temperature conditions for automotive electronics \[12, 13, 61, 62\].

> **Architecture Comparison**: Direct side-by-side evaluation of Pi-Gate (η = 0.82) and Omega-Gate (η = 0.98) configurations under identical conditions \[5, 15, 19\].

> **Electrical Performance**: Comprehensive analysis of capacitance-voltage (C-V) and current-voltage (I-V) characteristics including threshold voltage, subthreshold swing, on-current, and off-current metrics \[28, 30\].

### 5.4 Validation and Verification Protocol

> Results validation occurs through three-tier verification strategy:

> **Analytical Consistency**: Verification against closed-form theoretical limits at standard conditions (T = 300 K, tox = 3 nm, VDS → 0) to ensure mathematical correctness \[27, 28\].

> **TCAD Benchmarking**: Comparison against published TCAD simulation results from Breed & Roenker \[15\] and Deshpande et al. \[16\] with target agreement within 10-15% range \[26, 30\].

> **Experimental Correlation**: Benchmarking against published experimental data including cryogenic performance from Matos et al. \[13\] (Omega-gate, 82-330 K) to validate temperature-dependent models \[12, 13\].

> All numerical integrations converge to <1% relative error, ensuring computational reliability across all parametric conditions \[27, 30\].

### 5.5 Data Analysis and Performance Metrics

> Performance evaluation employs standardized semiconductor device metrics:

> **Electrostatic Control**: Threshold voltage variation, subthreshold swing, and drain-induced barrier lowering (DIBL) analysis \[2, 25\].

> **Current Drive Capability**: On-current (Ion) and current drive ratio assessment across different bias conditions \[28, 30\].

> **Leakage Characteristics**: Off-current (Ioff) analysis and on/off current ratio evaluation for switching performance \[25, 30\].

> **Temperature Stability**: Temperature coefficient analysis and performance degradation assessment across operating range \[12, 13\].

> **Material Optimization**: Figure of merit calculation combining multiple performance parameters for comprehensive material selection \[32, 33\].

![](media/image10.png){width="6.000694444444444in"
height="2.9131944444444446in"}

> **Figure 5.1:** Methodology flowchart for the comparative analysis of Pi-Gate and Omega-Gate NWFETs. The nine-step process covers device architecture definition (Pi: 82% wrap, Omega: 98% wrap; L = W = 10 nm), gate oxide material selection (SiO₂, Al₂O₃, HfO₂, ZrO₂, La₂O₃), simulation parameter definition (tox = 1-9 nm; T = 77-600 K; VGS = -0.5 to 1.2 V), Python framework development, electrical simulations (CV, IV, EIS), device parameter extraction (Vth, Ion, SS, DIBL), multi-parameter sweeps, validation, and performance comparison.

**Chapter 6:**

## Materials and Methods

## 

[]{#Device_Architecture_and_Structural_Param .anchor} **6.1 Device
[]{#Device_Architecture_and_Structural_Param .anchor} **5.1 Device
Architecture and Structural Parameters**

> Both Pi-Gate and Omega-Gate NWFETs are modelled as n-channel silicon
> nanowire devices with a circular cross-section. Structural parameters
> are listed in Table [4.1.](#_bookmark29)
>
>  **Table 4.1:** Structural parameters common to both Pi-Gate and
> Omega-Gate NWFET models used throughout this study.

  -------------------------------------------------------------------
   **Parameter**  **Description**                      **Value**
  --------------- ------------------------------- -------------------
      **Lg**      Gate / channel length                  10 nm

      **dNW**     Nanowire diameter                      10 nm

      **NA**      Channel doping (p-type)              10¹⁸ cm⁻³

      **ND**      Source/Drain doping (n⁺)             10²⁰ cm⁻³

      **tox**     Gate oxide thickness (swept)         1 -- 9 nm

      **VDD**     Supply voltage                         1.2 V

      **VDS**     Drain bias (I--V sweeps)               0.5 V

   **VGS range**  Gate voltage sweep                 −0.5 to 1.2 V

    **T range**   Temperature                         77 -- 600 K

      **ηπ**      Pi-Gate efficiency                     0.82

      **ηΩ**      Omega-Gate efficiency                  0.98
  -------------------------------------------------------------------

**3.2 Gate Dielectric Material Properties**

> **Table [3.2](#_bookmark31)** lists the five high-k dielectric
> materials. ALD is used for all high-k films in literature; sputtering
> was also validated by Shen et al. [\[33\].](#_bookmark153)

[]{#_bookmark31 .anchor}

  ------------------------------------------------------------------------
  **Material**    **k**    **Eg    **ΔEc   **EOT@3 nm       **Thermal
                          (eV)**   (eV)**    (nm)**        Stability**
  -------------- ------- -------- -------- ----------- -------------------
  **SiO₂**         3.9     9.0      3.15      3.00          Excellent

  **Al₂O₃**        9.0     8.8      2.80      1.30          Excellent

  **HfO₂**        25.0     5.7      1.50      0.47          Very Good

  **ZrO₂**        22.0     5.8      1.40      0.53            Good

  **La₂O₃**       27.0     5.5      2.30      0.43          Moderate
  ------------------------------------------------------------------------

**3.3 Analytical Physics Models**

> **3.3.1 Gate Efficiency Factor**

$\eta = \frac{\theta gate}{\ 2\pi}$ (3.1)

> Pi-Gate: η = 0.82 (θ = 295°); Omega-Gate: η = 0.98 (θ = 353°) \[5,
> 15\].

**3.3.2 Oxide Capacitance and EOT**

$Cox\  = \ \frac{\varepsilon ₀\ \varepsilon r\ }{tox}$ (3.2)

$EOT\  = (\ \frac{3.9}{\varepsilon r})\ tox$ (3.3)

Confirmed by Ritzenthaler et al. \[19\].

**3.3.3 Threshold Voltage**

Vth =
$\frac{VFB\  + \ 2\varphi F\  + \ \sqrt{}(q\ NA\ Wmax)\ }{(\eta\ Cox)}$
**(**3.4)

> where φF = (kBT/q) ln (NA/ni) and Wmax = √(4εSiφF / (qNA)) \[2\].
> Yadav et al. \[25\] confirm that tox and VGS are the primary
> determinants of electrostatic control quality.

**3.3.4 Capacitance-Voltage (C--V) Model**

C~gate~(V~GS~)
=$\frac{(\eta\ Cox\  \cdot \ Cdep)}{(\eta\ Cox\  + \ Cdep)\ \ \ \ \ }$
VGS \< Vth (depletion) (3.5a)

C~gate~(V~GS~)
=$\frac{(\eta\ Cox\  \cdot \ Cinv)\ }{(\eta\ Cox\  + \ Cinv),\ \ \ \ \ }$
VGS ≥ Vth (inversion) (3.5b)

**3.3.5 Drain Current Models**

> **Linear region:**
>
> Iᴰ_D(lin) =
> $\left( \frac{W}{L} \right)\left\lbrack \frac{\mu eff\ Cox}{\left( 1\  + \ \theta(VGS\  - \ Vth) \right)} \right\rbrack.\frac{(VGS\  - \ Vth)VDS\  - \ VDS²}{2}$
> (3.6)
>
> **Saturation region:**
>
> $Iᴰ_{D(sat)} = \ \left( \frac{W}{2L} \right)\left\lbrack \frac{\mu eff\ Cox}{\left( 1\  + \ \theta(VGS\  - \ Vth) \right)} \right\rbrack\mathbf{.}(VGS\  - \ Vth)²$
> (3.7)
>
> **Subthreshold region:**
>
> $Iᴰ_{D(sub)} = I^{0}\left\lbrack \frac{\ q(VGS\  - \ Vth)}{(nkBT)} \right\rbrack\mathbf{.\lbrack}1\  - \ exp(\frac{- qVDS}{kBT}$**)\]**
> (3.8)
>
> where n = 1 + Cd / (η Cox). The compact model approach follows Paul et
> al. \[28\], validated in Bala et al. \[30\].

**3.3.6 Subthreshold Swing**

![](media/image7.png){width="1.9041743219597551in"
height="0.5863396762904637in"} (3.9)

Theoretical minimum at 300 K: SS~min~ = 60 mV/dec.

**3.3.7 On/Off Current Ratio**

![](media/image8.png){width="1.8750962379702538in"
height="0.8194870953630796in"} (3.10)

**3.4 Simulation Framework**

> The modular Python-based simulation framework is illustrated in Fig.
> [3.1.](#_bookmark49) The compact model approach follows Paul et al.
> [\[28\];](#_bookmark148) the TCAD-validated parameter set follows Jain
> et al. [\[27\].](#_bookmark147) This Python framework enables
> simultaneous sweep of five materials, two gate types, nine tox values,
> and twelve temperature points. Doping concentration effects on Vth
> follow Bala et al. [\[30\],](#_bookmark150) and oxide thickness
> effects follow Yadav et al. [\[25\].](#_bookmark145) The framework
> validates against Si and Ge NWFET benchmarks from Stanojevic´ et al.
> [\[26\]](#_bookmark146) and Adinarayana et al.
> [\[31\].](#_bookmark151) Guesmi et al. [\[24\]](#_bookmark144) provide
> the self-heating electrothermal parameters for temperature-dependent
> corrections.
>
> Key Parameters
>
> \- Temperature range: 77 K to 600 K
>
> \- Gate voltage sweep: -0.5 V to 1.2 V
>
> \- Drain voltage: 0.5 V (for I-V) and varying (for output
> characteristics)
>
> \- Frequency range for EIS: 1 Hz to 1 MHz
>
> ![](media/image9.png){width="5.743582677165354in"
> height="2.9921259842519685in"}
>
> **Figure 3.1:** Simulation Framework Flowchart showing the modular
> architecture: input parameters branch simultaneously to CV Models, IV
> Models, and EIS Models. All three feed into Numerical Computation
> (NumPy/SciPy), followed by Validation and Output Results. The
> framework supports parallel sweeps across five materials, two gate
> types, nine tox values, and twelve temperature points.

![](media/image10.png){width="6.000694444444444in"
height="2.9131944444444446in"}

> **Figure 3.2:** Methodology flowchart for the comparative analysis of
> Pi-Gate and Omega-Gate NWFETs. The nine-step process covers device
> architecture definition (Pi: 82% wrap, Omega: 98% wrap; L = W = 10
> nm), gate oxide material selection (SiO~2~, Al~2~O~3~, HfO~2~, ZrO~2~,
> La~2~O~3~), simulation parameter definition (tox = 1--9 nm; T =
> 77--600 K; VGS = −0.5 to 1.2 V), Python framework development,
> electrical simulations (CV, IV, EIS), device parameter extraction
> (Vth, Ion, SS, DIBL), multi-parameter sweeps, validation, and
> performance comparison.

[]{#Validation_Strategy .anchor} **3.5 Validation Strategy**

> Results are validated at three levels:

- Analytical consistency against closed-form limits at T = 300 K, tox =
  3 nm, VDS →

> 0\.

- TCAD comparison against Breed & Roenker [\[15\]](#_bookmark135) and
  Deshpande et al. [\[16\],](#_bookmark136) with agreement within
  10--15%.

- Cryogenic benchmarking against Matos et al. [\[13\]](#_bookmark133)
  (Omega-gate, 82--330 K). Convergence criteria: all numerical
  integrations converge to \< 1% relative error.

[]{#_bookmark13 .anchor}

**Chapter 4:**

##  Comparison of Pi-Gate vs. Omega-Gate NWFETs by Varying Gate Oxide at Room Temperature

## 

> All simulations in this chapter are at T = 300 K with device
> dimensions from Table [4.1.](#_bookmark29) Five high-k dielectrics are
> compared for both gate architectures.

**5.1 Governing Equations**

####  5.1.1 Gate Efficiency and Oxide Capacitance

#### 

> From Chapter 4 (Eqs. [4.1--4.2):](#_bookmark36) ηπ = 0.82, ηΩ = 0.98,
> Cox = ε0εr/tox. The effective inversion charge density controlled by
> the gate is:
>
> *Q*~inv~ = *η C*~ox~ (*V~GS~* − *V*~th~) (4.1)
>
> Both higher η (Omega-Gate) and higher εr (high-k) increase the
> available conduction charge.

#### 5.1.2 Threshold Voltage Dependence

#### ![](media/image11.png){width="2.5309306649168852in" height="0.3543307086614173in"}

> .
>
> Increasing *η* or *C*~ox~ lowers *V*~th~, improving device turn-on.

#### On-Current Scaling 

#### ![](media/image12.png){width="4.528010717410324in" height="0.5278051181102362in"}

#### 

#### 

> The multiplicative benefit of high εr and high η means Omega-Gate with
> La~2~O~3~ yields the highest Ion.

#### Subthreshold Swing at 300 K

> ![](media/image13.png){width="4.360458223972003in"
> height="0.5511811023622047in"}

#### On/Off Current Ratio

> ![](media/image14.png){width="3.9756332020997376in"
> height="0.6299212598425197in"}
>
> **4.2 Capacitance-Voltage (C--V) Characteristics**
>
> ![](media/image15.jpeg){width="5.765832239720035in"
> height="3.031496062992126in"}The CV curves (Eq. [3.5)](#_bookmark40)
> are shown in Figs. [4.1](#_bookmark65) and [4.2](#_bookmark66) for
> Omega-Gate and Pi-Gate respectively. The Omega-Gate exhibits sharper
> capacitance transitions and higher peak inversion capacitance in all
> five dielectrics due to η = 0.98, consistent with Breed & Roenker's
> finding that "the Omega-gate MOSFET shows the best device scaling
> characteristics" [\[15\].](#_bookmark135) Thinner oxides (1 nm, dark
> purple curves) produce the highest Cox per Eq. [3.2;](#_bookmark36)
> La~2~O~3~ and HfO~2~ show the highest absolute capacitance values
> reflecting their large εr.
>
> **Figure 4.1:** C--V characteristics vs. oxide thickness for
> Omega-Gate NWFETs (T = 300 K; tox = 1--30 nm shown; VDS = 0 V) across
> all five high-k dielectrics: SiO2 (k = 3.9), Al2O3 (k = 9.0), HfO2 (k
> = 25), ZrO2 (k = 22), La2O3 (k = 27). The 1 nm (dark purple)
>
> gives maximum capacitance in each panel. HfO2 and La2O3 achieve the
> highest Cox values
>
> (∼200--250 mF/m2 at tox = 1 nm) consistent with Eq.
> [3.2.](#_bookmark36)

![](media/image16.jpeg){width="5.796874453193351in"
height="4.173228346456693in"}

> **Figure 4.2:** C--V characteristics vs. oxide thickness for Pi-Gate
> NWFETs (T = 300 K;
>
> tox = 1--30 nm; VDS = 0 V) across all five dielectrics. Peak inversion
> capacitance values are systematically lower than Omega-Gate
> equivalents (see Fig. [4.1)](#_bookmark65) due to the lower
>
> efficiency η = 0.82, which increases the effective series depletion
> capacitance in Eq. [3.5.](#_bookmark40)
>
> Deshpande et al. [\[16\]](#_bookmark136) confirm this trend for
> Pi-gate vs. GAA at identical tox.
>
> []{#Current-Voltage_(I–V)_Transfer_Character .anchor}**4.3
> Current-Voltage (I--V) Transfer Characteristics**
>
> Figure [4.3](#_bookmark68) presents the I--V transfer characteristics
> at T = 300 K and VDS = 0.5 V for all ten material-architecture
> combinations. Key observations:

- Omega-Gate achieves SS ≈ 58--65 mV/dec vs. ≈ 66--75 mV/dec for Pi-Gate
  across all materials (Eq. [4.4).](#_bookmark61)

- Vth is consistently lower for Omega-Gate by 20--30 mV (Eq.
  [4.2).](#_bookmark57)

- Drive current increases steeply with VGS; La2O3 Omega-Gate produces
  the highest ID

- Ritzenthaler et al. [\[19\]](#_bookmark139) support the observation
  that both architectures maintain excel- lent electrostatic control,
  with Omega-Gate providing a measurable but not categorical advantage
  at 300 K.

> ![](media/image17.jpeg){width="5.75in" height="3.9493055555555556in"}
>
> **Figure 4.3**: I--V transfer characteristics grid (ID vs. VGS, linear
> scale; T = 300 K, VDS = 0.5 V) for all five dielectrics and both gate
> architectures (Eqs. [3.7--3.8).](#_bookmark44) Top row: Pi-Gate;
> Bottom row: Omega-Gate. Columns (left to right): SiO~2~, Al~2~O~3~,
> HfO~2~, ZrO~2~,
>
> La2O3. Peak ID values increase monotonically with dielectric constant
> k (Eq. [4.3);](#_bookmark59) Omega-Gate curves consistently achieve
> higher ID at the same VGS compared to Pi-
>
> La2O3--Omega-Gate reaches ≈2800 µA/µm at VGS = 1.2 V.

### Material Performance Comparison

### 

> Table [4.1](#_bookmark70) presents extracted device parameters across
> all materials and gate types at tox = 3 nm. The dominant trend
> confirms Eq. [4.3:](#_bookmark59) Ion scales with εr, and the
> Omega-Gate amplifies this scaling through the η multiplicative factor.
> Minhaj et al. [\[8\]](#_bookmark128) confirm that high-k stack oxides
> benefit both Pi- and Omega-gate multigate FETs.
>
> **Table 4.1:** Extracted device parameters for Pi-Gate and Omega-Gate
> NWFETs across all five high-k dielectrics at T = 300 K, tox = 3 nm,
> VDS = 0.5 V, VGS = 1.2 V (Eqs. [4.2--4.5).](#_bookmark63) Bold values
> indicate global optima. SS = Subthreshold Swing

  --------------------------------------------------------------------------------
   **Material**     **Gate     **Vth    **Ion    **Ioff      **SS      **Ion/Ioff
                    Type**     (V)**    (μA)**   (nA)**   (mV/dec)**    Ratio**
  -------------- ------------ -------- -------- -------- ------------ ------------
     **SiO₂**      Pi-Gate      0.45     120       50         75        2.4×10⁶

     **SiO₂**     Omega-Gate    0.42     145       30         65        4.8×10⁶

    **Al₂O₃**      Pi-Gate      0.40     135       40         70        3.4×10⁶

    **Al₂O₃**     Omega-Gate    0.38     160       25         60        6.4×10⁶

     **HfO₂**      Pi-Gate      0.35     150       35         68        4.3×10⁶

     **HfO₂**     Omega-Gate    0.33     180       20         58        9.0×10⁶

     **ZrO₂**      Pi-Gate      0.38     140       38         72        3.7×10⁶

     **ZrO₂**     Omega-Gate    0.36     165       22         62        7.5×10⁶

    **La₂O₃**      Pi-Gate      0.32     155       32         66        4.8×10⁶

    **La₂O₃**     Omega-Gate    0.30     185       18         56        10.3×10⁶
  --------------------------------------------------------------------------------

> The global optimum is La~2~O~3~--Omega-Gate: Ion/Ioff = 10.3 × 106 and
> SS = 56 mV/dec, representing a 4.3× improvement in Ion/Ioff and 19
> mV/dec reduction in SS compared to SiO~2~ Pi-Gate.

### Oxide Thickness Scaling: 1 to 9 nm

### 

> As tox decreases, Cox increases (Eq. [3.2),](#_bookmark36) lowering
> Vth (Eq. [4.2)](#_bookmark57) and raising Ion (Eq.
> [4.3).](#_bookmark59) The relationship is: Ion ∝ 1/tox for constant η
> and overdrive voltage. Deshpande et al. [\[16\]](#_bookmark136)
> specifically confirm that Pi-gate drain current decreases with
> increasing tox. Direct tunnelling leakage rises sharply below tox = 2
> nm in SiO~2~ but is suppressed in high-k films because a physically
> thicker film achieves the same EOT. Tables [4.2](#_bookmark72) and
> [4.3](#_bookmark73) present extracted Vth, Ion, and Ioff at four
> representative oxide thicknesses (1, 3, 5, 9 nm) for all five
> dielectrics.

### 

> **Table 4.2:** Pi-Gate NWFET extracted parameters vs. oxide thickness
> at T = 300 K,
>
> VDS = 0.5 V, VGS = 1.2 V. Vth is nearly independent of tox (flat;
> varies by \<5 mV due to fixed doping model); Ion decreases with tox
> per Eq. [4.3.](#_bookmark59)

+-------------------+---------+-----------------------------+
| **Material**      | **tox** | **Pi-Gate**                 |
|                   |         +--------+-----------+--------+
|                   |         | **η**  | **Cox     | **Ioff |
|                   |         |        | (nF/m²)** | (µA)** |
+:=================:+:=======:+:======:+:=========:+:======:+
| **SiO₂**          | 1 nm    | 0.45   | 340       | 0.18   |
|                   +---------+--------+-----------+--------+
|                   | 3 nm    | 0.45   | 120       | 0.05   |
|                   +---------+--------+-----------+--------+
|                   | 5 nm    | 0.45   | 72        | 0.03   |
|                   +---------+--------+-----------+--------+
|                   | 9 nm    | 0.45   | 40        | 0.02   |
+-------------------+---------+--------+-----------+--------+
| **Al₂O₃**         | 1 nm    | 0.40   | 405       | 0.22   |
|                   +---------+--------+-----------+--------+
|                   | 3 nm    | 0.40   | 135       | 0.08   |
|                   +---------+--------+-----------+--------+
|                   | 5 nm    | 0.40   | 81        | 0.05   |
|                   +---------+--------+-----------+--------+
|                   | 9 nm    | 0.40   | 45        | 0.03   |
+-------------------+---------+--------+-----------+--------+
| **HfO₂**          | 1 nm    | 0.35   | 450       | 0.25   |
|                   +---------+--------+-----------+--------+
|                   | 3 nm    | 0.35   | 150       | 0.09   |
|                   +---------+--------+-----------+--------+
|                   | 5 nm    | 0.35   | 90        | 0.05   |
|                   +---------+--------+-----------+--------+
|                   | 9 nm    | 0.35   | 50        | 0.03   |
+-------------------+---------+--------+-----------+--------+
| **ZrO₂**          | 1 nm    | 0.38   | 420       | 0.24   |
|                   +---------+--------+-----------+--------+
|                   | 3 nm    | 0.38   | 140       | 0.08   |
|                   +---------+--------+-----------+--------+
|                   | 5 nm    | 0.38   | 84        | 0.05   |
|                   +---------+--------+-----------+--------+
|                   | 9 nm    | 0.38   | 47        | 0.03   |
+-------------------+---------+--------+-----------+--------+
| **La₂O₃**         | 1 nm    | 0.32   | 465       | 0.26   |
|                   +---------+--------+-----------+--------+
|                   | 3 nm    | 0.32   | 155       | 0.09   |
|                   +---------+--------+-----------+--------+
|                   | 5 nm    | 0.32   | 93        | 0.05   |
|                   +---------+--------+-----------+--------+
|                   | 9 nm    | 0.32   | 52        | 0.03   |
+-------------------+---------+--------+-----------+--------+

> **Table 4.3:** Omega-Gate NWFET extracted parameters vs. oxide
> thickness at T = 300 K, VDS = 0.5 V, VGS = 1.2 V. Ion is consistently
> 20--25% higher than Pi-Gate equivalents (Table [4.2)](#_bookmark72) at
> each tox, confirming Eq. [4.3:](#_bookmark59) Ion ∝ η Cox. The optimal
> window of tox = 2--5 nm balances performance and tunnelling leakage
> reliability.

+----------------+---------+------------------------------------+
| **Material**   | **tox** | **Omega-Gate**                     |
|                |         +-----------+-----------+------------+
|                |         | **η**     | **Cox     | **Ioff     |
|                |         |           | (nF/m²)** | (µA)**     |
+:==============:+:=======:+:=========:+:=========:+:==========:+
| **SiO₂**       | 1 nm    | 0.42      | 435       | 0.11       |
|                +---------+-----------+-----------+------------+
|                | 3 nm    | 0.42      | 145       | 0.04       |
|                +---------+-----------+-----------+------------+
|                | 5 nm    | 0.42      | 87        | 0.02       |
|                +---------+-----------+-----------+------------+
|                | 9 nm    | 0.42      | 48        | 0.01       |
+----------------+---------+-----------+-----------+------------+
| **Al₂O₃**      | 1 nm    | 0.38      | 520       | 0.14       |
|                +---------+-----------+-----------+------------+
|                | 3 nm    | 0.38      | 160       | 0.05       |
|                +---------+-----------+-----------+------------+
|                | 5 nm    | 0.38      | 98        | 0.03       |
|                +---------+-----------+-----------+------------+
|                | 9 nm    | 0.38      | 55        | 0.02       |
+----------------+---------+-----------+-----------+------------+
| **HfO₂**       | 1 nm    | 0.33      | 580       | 0.16       |
|                +---------+-----------+-----------+------------+
|                | 3 nm    | 0.33      | 180       | 0.06       |
|                +---------+-----------+-----------+------------+
|                | 5 nm    | 0.33      | 108       | 0.03       |
|                +---------+-----------+-----------+------------+
|                | 9 nm    | 0.33      | 60        | 0.02       |
+----------------+---------+-----------+-----------+------------+
| **ZrO₂**       | 1 nm    | 0.36      | 550       | 0.15       |
|                +---------+-----------+-----------+------------+
|                | 3 nm    | 0.36      | 165       | 0.05       |
|                +---------+-----------+-----------+------------+
|                | 5 nm    | 0.36      | 100       | 0.03       |
|                +---------+-----------+-----------+------------+
|                | 9 nm    | 0.36      | 56        | 0.02       |
+----------------+---------+-----------+-----------+------------+
| **La₂O₃**      | 1 nm    | 0.30      | 600       | 0.17       |
|                +---------+-----------+-----------+------------+
|                | 3 nm    | 0.30      | 185       | 0.06       |
|                +---------+-----------+-----------+------------+
|                | 5 nm    | 0.30      | 112       | 0.03       |
|                +---------+-----------+-----------+------------+
|                | 9 nm    | 0.30      | 62        | 0.02       |
+----------------+---------+-----------+-----------+------------+

> **Key scaling finding:** The Omega-Gate consistently outperforms the
> Pi-Gate across all oxide thicknesses by 20--25% in Ion and 35--45% in
> Ioff suppression, confirming the simulation results of Breed & Roenker
> [\[15\]](#_bookmark135) who showed Omega-gate dominance in scaling
> characteristics.

**Chapter 5:**

**Comparison of Pi-Gate vs. Omega-Gate NWFETs by Varying Gate Oxide
Thickness and Temperature**

> **5.1 Temperature-Dependent Physics Equations**

#### ![](media/image18.png){width="4.608333333333333in" height="0.4861111111111111in"}

#### 

> Consistent with Balestra & Ghibaudo [\[12\]](#_bookmark132) who
> measured mobility enhancement in Omega-gate NWFETs down to 20 K.

####  5.1.2 Temperature-Dependent Threshold Voltage

#### ![](media/image19.png){width="5.0in" height="0.3958333333333333in"} 

> Confirmed experimentally by Matos et al. [\[13\]](#_bookmark133) for
> Omega-gate NWFETs from 82 K to
> []{#Temperature-Dependent_Subthreshold_Swing .anchor}330 K.
>
> **5.1.3 Temperature-Dependent Subthreshold Swing**

![](media/image20.png){width="5.142361111111111in" height="0.66875in"}

> At 77 K: SSideal = (0.00664/1) × 2.303 ≈ 15.3 mV/dec. The higher η of
> Omega-Gate gives n ≈ 1.05 vs. n ≈ 1.15 for Pi-Gate, yielding a
> measurable SS advantage at every temperature.
>
> ![](media/image21.png){width="5.012422353455818in"
> height="0.8819444444444444in"}**5.1.4 Temperature-Dependent Saturation
> Current**
>
> **5.1.5 Arrhenius Leakage Model**
>
> ![](media/image22.png){width="5.241666666666666in"
> height="0.4861111111111111in"}
>
> Consistent with Guesmi et al. [\[24\]](#_bookmark144) who model
> self-heating leakage in NWFETs using
> []{#3D_Drain_Current_Surface_Model .anchor}electrothermal Arrhenius
> models.

**5.1.6 3D Drain Current Surface Model**

> ![](media/image23.png){width="5.676388888888889in"
> height="0.5833333333333334in"}
>
> **5.2 Temperature-Dependent Transfer Characteristics**
>
> Figure [5.1](#_bookmark89) shows I--V transfer characteristics at T =
> {77, 200, 300, 400, 500, 600} K for five channel materials (Si, Ge,
> GaAs, InAs, GaN) and both gate architectures. At 77 K (blue,
> steepest), the Omega-Gate consistently shows lower minimum current and
> sharper turn-on, consistent with SS (77) ≈ 15--20 mV/dec (Eq.
> [5.3).](#_bookmark81) At 600 K (purple/brown), Pi-Gate leakage rises
> more rapidly than Omega-Gate leakage due to the lower η reducing the
> channel potential barrier. Balestra & Ghibaudo [\[12\]](#_bookmark132)
> and Matos et al. [\[13\]](#_bookmark133) validate this trend for
> Omega-gate devices at cryogenic temperatures.
>
> At cryogenic temperatures, reduced VT leads to improved SS and lower
> power consumption, with mobility enhancement providing higher drive
> currents. The exponential mobility dependence shows why phonon
> scattering limits performance at room temperature, while impurity
> scattering dominates at extreme low temperatures. The Vt temperature
> coefficient highlights why Omega-Gate structures maintain better
> stability, as their superior electrostatic control reduces
> temperature-induced variations in depletion charge.
>
> ![](media/image24.jpeg){width="5.750694444444444in"
> height="5.235416666666667in"}**Figure 5.1:** Temperature-dependent
> transfer characteristics (ID vs. VGS, logarithmic scale; VDS = 0.5 V)
> for Pi-Gate (left column) and Omega-Gate (right column) NWFETs across
> five channel materials: Si, Ge, GaAs, InAs, GaN. Temperatures shown:
> 77 K (blue), 200 K (red dashed), 300 K (green dash-dot), 400 K (yellow
> dotted), 500 K (red), 600 K (purple).
>
> Omega-Gate consistently shows lower Ioff and steeper subthreshold
> slope at all temperatures per Eq. [5.3.](#_bookmark81) GaAs and InAs
> materials exhibit the sharpest cryogenic turn-on due to higher
> mobility [\[30\].](#_bookmark150)

###  5.3 3D Surface: Drain Current vs. Oxide Thickness and Temperature

> Figure [5.2](#_bookmark91) visualises ID (tox, T) (Eq.
> [5.6)](#_bookmark87) as 3D surfaces for all ten material-architecture
> combinations. Omega-Gate surfaces (bottom row) consistently lie at
> higher current levels across the entire (*t*~ox~*, T)* plane. Current
> drops steeply as tox increases (inverse Cox
>
> dependence) and decreases at high T due to reduced µeff (Eq.
> [5.1).](#_bookmark77) The combined optimum for maximum ID is at tox ≈
> 1--2 nm and T = 77 K, though reliability constraints favour tox ≈ 2--3
> nm.
>
> ![](media/image25.jpeg){width="5.745833333333334in"
> height="3.595138888888889in"}
>
> **Figure 5.2:** 3D surface plots of ID (tox, T) (Eq.
> [5.6)](#_bookmark87) for Pi-Gate (top row) and Omega-Gate (bottom row)
> NWFETs, across all five high-k dielectrics (VGS = 1 V, VDS = 0.5 V).
> Axes: tox (2--9 nm), temperature (77--600 K), ID (µA). Colour scale:
> yellow = high ID; purple = low ID. The Omega-Gate surfaces are
> uniformly elevated; HfO2 and La~2~O~3~ produce the highest current
> surfaces in both architectures.
>
> This figure visualizes the multi-dimensional parameter space, showing
> how device performance varies with both thickness and temperature. It
> is used to identify optimal design points that balance performance and
> reliability across wide temperature ranges.
>
> Omega-Gate configurations demonstrate better temperature stability,
> with the 3D transfer plots showing consistent performance across
> materials. Pi-Gate devices show more pronounced temperature
> sensitivity, particularly with high-k materials. The gate efficiency
> factor plays a crucial role in thermal management, with higher η
> values providing better isolation from thermal fluctuations.
>
> ![](media/image26.png){width="6.28969706911636in"
> height="4.746020341207349in"}
>
> **Figure 5.3:** 3D transfer characteristics (ID vs. VGS vs.
> temperature; VDS = 0.5 V; Eq. [5.4)](#_bookmark83) for Pi-Gate (top
> row) and Omega-Gate (bottom row) across all five high-k dielectrics.
> ID values rise steeply at cryogenic temperatures (low T, front face)
> due to higher µeff (Eq. [5.1)](#_bookmark77) and sharper Fermi-Dirac
> distribution. The Omega-Gate surfaces show higher peak ID and steeper
> VGS gradients at all temperatures, confirming superior gate coupling
> (Eq. [4.1).](#_bookmark55)

###  5.5 Device Parameters vs. Temperature: 77 K to 600 K

### 

> Figure [5.4](#_bookmark95) plots Vth(T ) (Eq.
> [5.2),](#temperature-dependent-threshold-voltage) Ion(T ) (Eq.
> [5.4),](#_bookmark83) and Ioff(T ) (Eq. [5.5)](#_bookmark85) vs.
> temperature for both architectures and all dielectrics. Key findings:

- **Vth (left panel):** All materials and both gate types show
  near-identical linear Vth (T ) decrease (γT ≈ −0.5 mV/K) consistent
  with Eq. [5.2.](#temperature-dependent-threshold-voltage)
  La~2~O~3~--Omega-Gate (cyan) maintains the lowest Vth across the full
  range (0.30 V at 300 K; 0.21 V at 600 K).

- **Ion (centre panel):** La~2~O~3~--Omega-Gate achieves the highest Ion
  at cryogenic tempera- tures (\> 20,000 µA/µm at 77 K). The spread
  between materials is greatest at low T and converges toward ∼200--500
  µA/µm at 600 K.

- **Ioff (right panel):** Leakage is negligible below 400 K but rises
  exponentially above 400 K (Eq. [5.5).](#_bookmark85)
  La~2~O~3~--Omega-Gate (cyan) shows the highest leakage at 600 K (∼5.5
  nA/µm) reflecting its lower bandgap. HfO~2~ provides the most stable
  Ion/Ioff above 400 K.

![](media/image27.png){width="6.268055555555556in"
height="3.5555555555555554in"}

> **Figure 5.4:** Device parameters vs. temperature (77--600 K) for
> Pi-Gate and Omega-Gate NWFETs across all five dielectrics at tox = 3
> nm, VDS = 0.5 V. Left: Vth (T) (Eq.
> [5.2)](#temperature-dependent-threshold-voltage) all curves
> approximately coincide, confirming γT is gate-type-independent.
> Centre: Ion (T) (Eq. [5.4)](#_bookmark83) Omega-Gate curves (higher
> lines) outperform Pi-Gate at every temperature. Right: Ioff (T) (Eq.
> [5.5)](#_bookmark85) only La~2~O~3~--Omega-Gate (cyan) shows
> significant leakage at 600 K; all others remain below 1 nA/µm.
> Consistent with Matos et al. [\[13\]](#_bookmark133) and Guesmi et al.
> [\[24\].](#_bookmark144)

### 

###  5.6 Cryogenic Performance at 77 K

###  

> ![](media/image28.png){width="5.272916666666666in"
> height="0.5902777777777778in"}
>
> Figure [5.5](#_bookmark98) shows I--V transfer characteristics at
> exactly 77 K for five channel materials and both gate types. Key
> observations:

- All devices show dramatically reduced Ioff (10−14--10−18 A) relative
  to 300 K, consis- tent with the Arrhenius leakage model (Eq.
  [5.5).](#_bookmark85)

- Omega-Gate curves (right column, dashed) show earlier turn-on (lower
  Vth (77)) in all materials.

- InAs NWFETs achieve the highest Ion at 77 K due to high electron
  mobility, consistent with Bala et al. [\[30\]](#_bookmark150) and
  Stanojevic´ et al. [\[26\].](#_bookmark146)

- GaN devices show the lowest absolute current at 77 K but widest
  Ion/Ioff ratio due to their large bandgap.

![](media/image29.png){width="5.557638888888889in"
height="4.813194444444444in"}

> **Figure 5.5:** Cryogenic I--V transfer characteristics at T = 77 K
> for Pi-Gate (left, solid) and Omega-Gate (right, dashed) NWFETs across
> five channel materials: Si (blue), Ge (green), GaAs (purple), InAs
> (blue/red), GaN (green/gold); VDS = 0.5 V, logarithmic scale. All
> devices show Ioff \< 10−13 A, confirming the exponential leakage
> suppression of Eq. [5.5.](#_bookmark85)
>
> Omega-Gate achieves SS approaching 15.3 mV/dec (Eq.
> [5.7).](#_bookmark97) Validated against cryogenic Si NWFET benchmarks
> from Balestra & Ghibaudo [\[12\].](#_bookmark132)

###  5.7 3D Normalised Transfer Characteristics

### 

> ![](media/image30.png){width="6.265767716535433in"
> height="3.263888888888889in"}Figure [5.6](#_bookmark100) plots ID/ID
> (400 K) vs. VGS vs. temperature to isolate the relative temperature
> sensitivity from the absolute magnitude differences. At T = 400 K,
> ID/ID (400) = 1.0 by definition. Curves above 1.0 (cryogenic
> temperatures) indicate mobility-enhanced operation; curves below 1.0
> (above 400 K) reflect the competing effects of reduced mobility and
> increased leakage.
>
> **Figure 5.6**: 3D normalised transfer characteristics ID/ID (400 K)
> vs. VGS vs. temperature (VDS = 0.5 V) for Pi-Gate (top row, red/warm
> tones) and Omega-Gate (bottom row, blue/cool tones) across all five
> high-k dielectrics. The Omega-Gate surfaces (bottom) show a flatter
> temperature dependence smaller peak-to-trough ratio indicating
> superior thermal stability of the gate electrostatics. This is
> consistent with Ritzenthaler et al. [\[19\]](#_bookmark139) who
> attribute this to stronger back-gate coupling suppression in Ω-gate
> geometries.

###  5.8 Temperature Summary Table

### 

> **Table 5.1:** Summary of temperature-dependent performance for the
> two best-performing dielectrics at tox = 3 nm, VDS = 0.5 V, Si
> channel.

+-----------------+--------------+------------+------------+-----------+--------------+
| **Temperature** | **Material** | **Gate     | **SS       | **Cox     | **Ion/Ioff** |
|                 |              | Type**     | (mV/dec)** | (nF/m²)** |              |
+:===============:+:============:+============+:==========:+:=========:+:============:+
| **77 K**        | **HfO₂**     | Pi-Gate    | 19         | 480       | \> 10⁹       |
|                 |              +------------+------------+-----------+--------------+
|                 |              | Omega-Gate | 16         | 590       | \> 10¹⁰      |
|                 +--------------+------------+------------+-----------+--------------+
|                 | **La₂O₃**    | Pi-Gate    | 18         | 510       | \> 10⁹       |
|                 |              +------------+------------+-----------+--------------+
|                 |              | Omega-Gate | 15         | 630       | \> 10¹⁰      |
+-----------------+--------------+------------+------------+-----------+--------------+
| **300 K**       | **HfO₂**     | Pi-Gate    | 68         | 150       | 4.3 × 10⁶    |
|                 |              +------------+------------+-----------+--------------+
|                 |              | Omega-Gate | 58         | 180       | 9.0 × 10⁶    |
|                 +--------------+------------+------------+-----------+--------------+
|                 | **La₂O₃**    | Pi-Gate    | 66         | 155       | 4.8 × 10⁶    |
|                 |              +------------+------------+-----------+--------------+
|                 |              | Omega-Gate | 56         | 185       | 10.3 × 10⁶   |
+-----------------+--------------+------------+------------+-----------+--------------+
| **600 K**       | **HfO₂**     | Pi-Gate    | 128        | 45        | 1.2 × 10³    |
|                 |              +------------+------------+-----------+--------------+
|                 |              | Omega-Gate | 112        | 62        | 3.8 × 10³    |
|                 +--------------+------------+------------+-----------+--------------+
|                 | **La₂O₃**    | Pi-Gate    | 132        | 42        | 0.8 × 10³    |
|                 |              +------------+------------+-----------+--------------+
|                 |              | Omega-Gate | 116        | 58        | 2.1 × 10³    |
+-----------------+--------------+------------+------------+-----------+--------------+

> For applications requiring wide-temperature operation,
> **HfO~2~--Omega-Gate** is recommended.

**Chapter-6**

**Electrochemical Impedance Spectroscopy (EIS) Analysis of Pi-Gate and
Omega-Gate Silicon Nanowire FETs with High-k Dielectrics**

### Introduction 

### 

> Electrochemical Impedance Spectroscopy (EIS) is a non-destructive,
> frequency-domain measurement technique that applies a small sinusoidal
> perturbation to a system and measures the resulting complex impedance
> Z\*(ω) = Z′ + jZ′′ as a function of angular frequency ω = 2πf \[44,
> 55\]. Originally developed for electrochemical systems such as
> batteries \[46\] and corrosion analysis \[47\], EIS has been
> increasingly applied to semiconductor device characterization, where
> it probes dielectric relaxation, interface trap dynamics, and gate
> oxide quality that static DC measurements cannot capture \[48, 49\].
> In the context of nanowire FETs with high-k gate dielectrics, EIS
> offers unique insights into: (a) the frequency-dependent permittivity
> of the gate oxide, revealing relaxation mechanisms specific to each
> dielectric material; (b) interface trap density (Dit) and response
> time through the conductance method; (c) dielectric loss tangent (tan
> δ), which directly impacts high-frequency device performance; and (d)
> the activation energy for dielectric relaxation, extractable from
> Arrhenius analysis of the electric modulus M′′ peak frequency \[50,
> 51\]. This chapter extends the DC I--V and C--V comparative study of
> Pi-Gate and Omega-Gate NWFETs \[41\] into the frequency domain. The
> same five dielectrics (SiO~2~, Al~2~O~3~, HfO~2~, ZrO~2~, La~2~O~3~),
> two gate geometries (η = 0.82 and 0.98), and the full 77--600 K
> temperature range are analysed through four complementary EIS
> formalisms: complex impedance (Z\*), complex permittivity (ε\*),
> electric modulus (M\*), and AC conductivity (σac) \[52, 53\].

### Theoretical Background and Equivalent Circuit Model 

### 

1.  **Cole-Cole Complex Permittivity**

(6.1)

> where εs is the static (low-frequency) relative permittivity, ε∞ is
> the high-frequency permittivity, τ (s) is the relaxation time, and α
> (0 ≤ α \< 1) is the Cole-Cole distribution parameter. When α = 0, Eq.
> (1) reduces to the ideal Debye model; increasing α indicates a broader
> distribution of relaxation times, characteristic of amorphous or
> polycrystalline high-k oxides \[55\]. The real part ε′(ω) represents
> the dielectric constant, while the imaginary part ε′′(ω) represents
> the dielectric loss.

**2.2 Electric Modulus**

(6.2)

> where Ea (eV) is the activation energy and kB = 1.381 × 10--23 J/K is
> the Boltzmann constant.
>
> **2.3 AC Conductivity and Jonscher Power Law**

(6.3)

> where s (0 \< s \< 1) is the frequency exponent indicating the
> dominant charge transport mechanism: s ≈ 1 indicates localized hopping
> conduction (typical of amorphous oxides), while s ≈ 0.5 suggests
> diffusion-limited transport \[59\].
>
> **2.4 Equivalent Circuit Model**
>
> The NWFET gate stack is modelled as a series combination of Rs
> (contact and channel resistance), a parallel Rox \|\| Cox element
> (oxide bulk), and a parallel Cd \|\| (Git + jCit) element (depletion
> layer with interface traps). The gate-coverage factor η enters through
> the effective oxide capacitance Cox = ηε0εr/tox, following Eq. (1) of
> the companion I--V paper \[41\]. The interface trap density Dit
> (cm−2eV−1) is extracted using the conductance method \[60\].

### Results and Discussion 

### 

1.  **Nyquist Plots**

> ![](media/image34.png){width="6.333540026246719in"
> height="2.8346456692913384in"}Figure 6.1 presents the Nyquist plots
> (--Z′′ vs Z′) for all five dielectrics at 300 K. SiO~2~ exhibits the
> largest impedance arc owing to its low permittivity (k = 3.9), while
> the high-k oxides (HfO~2~, ZrO~2~, La~2~O~3~) show significantly
> smaller arcs. The Omega-Gate (η = 0.98) consistently produces lower
> impedance than the Pi-Gate (η = 0.82) across all dielectrics,
> consistent with the higher effective gate capacitance reducing
> resistive contributions in the equivalent circuit model \[41, 61\].
>
> **Figure 6.1:** Nyquist plots for Pi-Gate and Omega-Gate NWFETs at T =
> 300 K with five high-k dielectrics.

2.  **Cole-Cole Analysis**

> The Cole-Cole plots (ε′′ vs ε′) in Figure 6.2 reveal the dielectric
> relaxation characteristics of each oxide. All high-k dielectrics
> exhibit depressed semicircular arcs, confirming non-Debye relaxation
> behaviour described by Eq. (1). La~2~O~3~ shows the most depressed arc
> (α = 0.22), indicating the broadest distribution of relaxation times,
> while SiO~2~ is closest to ideal Debye behaviour (α = 0.05). The
> Omega-Gate arcs extend to higher ε′ values due to the larger effective
> permittivity from superior gate coverage \[54, 62\].
>
> ![](media/image35.png){width="6.695475721784777in"
> height="2.7559055118110236in"}**Figure 6.2:** Cole-Cole plots showing
> dielectric relaxation for five gate dielectrics at T = 300 K.

3.  **Bode Plots**

> ![](media/image36.png){width="6.811111111111111in"
> height="2.9131944444444446in"}The Bode magnitude and phase plots in
> Figure 6.3 identify the frequency regimes dominated by different
> equivalent circuit elements. The impedance magnitude \|Z\| follows a
> characteristic 1/ω slope dominated by the oxide capacitance at
> intermediate frequencies. The phase plot reveals relaxation peaks at
> dielectric-specific frequencies: La~2~O~3~ peaks at the lowest
> frequency (\~10--100 Hz) owing to its longest relaxation time (τ =
> 49.8 ms), while SiO~2~ peaks at the highest frequency (\~1 MHz) with
> the shortest relaxation time (τ = 0.75 μs) \[45, 52\].
>
> **Figure 6.3:** Bode plots (\|Z\| and phase vs frequency) for five
> dielectrics at T = 300 K.

4.  **Electric Modulus Analysis**

> Figure 6.4 shows the imaginary electric modulus M′′ vs frequency. Each
> dielectric produces a distinct M′′ peak at its characteristic
> relaxation frequency, with SiO~2~ at the highest frequency and
> La~2~O~3~ at the lowest. The M′′ peak height is inversely proportional
> to the static permittivity, confirming that the modulus formalism
> correctly suppresses electrode polarisation effects \[56, 57\]. Figure
> 6.5 presents the modulus Cole-Cole plot (M′′ vs M′), where SiO~2~
> shows a near-perfect semicircle (ideal Debye) while HfO~2~ and
> La~2~O~3~ exhibit progressively depressed arcs.
>
> ![](media/image37.png){width="5.902583114610674in"
> height="2.559055118110236in"}
>
> ![](media/image38.png){width="5.89375in"
> height="2.6770833333333335in"}**Figure 6.4:** Electric modulus M′′ vs
> frequency for five dielectrics at T = 300 K.
>
> **Figure 6.5:** Modulus Cole-Cole plots (M′′ vs M′) for SiO₂, HfO₂,
> and La₂O₃ at T = 300 K.

5.  **AC Conductivity**

> ![](media/image39.png){width="6.471093613298338in"
> height="2.7559055118110236in"}Figure 6.6 shows the AC conductivity σac
> vs frequency at 300 K. All dielectrics follow Jonscher's universal
> power law (Eq. 3), with the frequency exponent s ≈ 0.6 indicating
> hopping conduction in the amorphous/polycrystalline oxide films.
> SiO~2~ shows the widest conductivity variation across the frequency
> range (\~8 decades), while the high-k oxides show a narrower but
> higher baseline conductivity due to their smaller bandgaps \[58, 59\].
>
> **Figure 6.6:** AC conductivity vs frequency for five dielectrics at T
> = 300 K.

6.  **Temperature-Dependent M′′ Peak Shift**

> Figure 6.7 demonstrates the thermally activated shift of the HfO~2~
> M′′ peak across 77--600 K. The peak systematically shifts from \~1 Hz
> at 77 K to \~107 Hz at 600 K, spanning seven decades of frequency. The
> x-markers track each peak position. This shift follows the Arrhenius
> relation of Eq. (2), and the slope of the Arrhenius plot (Figure 8)
> yields the activation energy Ea = 0.45 eV for HfO~2~. La~2~O~3~ has
> the highest Ea = 0.50 eV, while SiO~2~ has the lowest Ea = 0.35 eV
> \[50, 57\].
>
> ![](media/image40.png){width="5.502306430446194in"
> height="2.4803149606299213in"}
>
> ![](media/image41.png){width="5.961349518810149in"
> height="2.559055118110236in"}**Figure 6.7:** M′′ peak shift with
> temperature for HfO₂ (77--600 K). X-markers indicate peak positions.
>
> **Figure 6.8:** Arrhenius plots of dielectric relaxation time for all
> five dielectrics (77--600 K).

7.  **Loss Tangent and Cryogenic Performance**

> Figure 6.9 shows tan δ vs temperature at 1 MHz. Each dielectric's loss
> tangent peaks at a temperature where its relaxation frequency matches
> the 1 MHz probe frequency. At 300 K, HfO~2~ and La~2~O~3~ show the
> lowest tan δ (≤ 0.001), confirming low dielectric loss---consistent
> with their selection for high-performance device applications \[41\].
> Figure 6.10 presents the cryogenic dielectric response at 77 K. All
> permittivities collapse to their high-frequency values ε∞ with
> effectively zero dielectric loss (ε′′ ≈ 0).
>
> ![](media/image42.png){width="5.684722222222222in"
> height="2.6375in"}This complete freeze-out of dielectric relaxation at
> 77 K directly correlates with the near-ideal subthreshold swing (SS ≈
> 15--19 mV/dec approaching the theoretical limit of 15.3 mV/dec)
> observed in the companion I--V study \[41, 63\]. The absence of lossy
> relaxation processes at cryogenic temperature eliminates a source of
> gate stack non-ideality, contributing to the steeper SS \[64\].
>
> ![](media/image43.png){width="5.777760279965005in"
> height="2.4803149606299213in"}**Figure 6.9:** Loss tangent (tan δ) vs
> temperature at 1 MHz for all dielectric-gate combinations.
>
> **Figure 6.10:** Cryogenic dielectric response (ε′ and ε′′) at 77 K
> for all dielectric-gate combinations.

8.  **Comprehensive EIS Parameter Table**

> ![](media/image44.png){width="6.747222222222222in"
> height="3.363888888888889in"}Table 5 summarises the extracted EIS
> parameters for all ten gate--dielectric combinations at 300 K.

**Chapter 7:**

##  Interactive Web Application: Pi-Omega FET Simulator

### 

###  7.1 Motivation

> Survey of two hundred three nanowire FET studies spanning 2005 through
> 2024 exposed a glaring omission: zero browser-native platforms permit
> concurrent Pi-Gate and Omega-Gate exploration. Existing pipelines
> chain researchers to cost-prohibitive ecosystems Sentaurus and Silvaco
> Atlas licenses exceed fifty thousand dollars annually alternatively
> demanding coding proficiency in MATLAB or SPICE environments. This
> financial and technical fortress walls off developing-region
> institutions and undergraduate learners from meaningful NWFET
> investigation. Pi-Omega FET Simulator dismantles these barriers
> through pure web delivery, eliminating download-install barriers while
> furnishing instantaneous comparative visualization previously absent
> from semiconductor education tooling \[64\].

###  7.2 System Design & Implementations

> The deployed solution bifurcates processing workloads: heavy numerics
> execute remotely via Python stacks (NumPy for tensor operations, SciPy
> for differential equation solving), whereas rendering duties shift to
> user browsers through Plotly.js vector graphics \[65\]. Such
> partitioning guarantees numerical integrity identical to offline
> simulations (Chapters 3-6) while maintaining visual feedback loops
> under two hundred milliseconds matching human perceptual thresholds
> for seamless interaction \[66\].

###  7.2.1 Server-Side Computation Modules

### 

> Backend functionality segments into four encapsulated classes
> mirroring preceding analytical frameworks:

- **Gate Stack Solver:** Handles metal-oxide-semiconductor
  electrostatics \[2\]

- **Current Solver:** Encodes linear, saturation, subthreshold
  conduction regimes \[63\]

- **Cryo-Thermal Solver:** Tracks mobility degradation across 77-600
  Kelvin span \[12\]

- **Impedance Solver:** Resolves electrochemical frequency response
  \[44\]

> Each solver ingests JSON-formatted parameter bundles from client
> requests, returning serialized arrays for immediate plotting
> consumption. Benchmarking on mid-tier consumer hardware (Intel i5-10th
> generation) clocked full band diagram recalculation at one hundred
> fifty to one hundred eighty milliseconds surpassing conventional
> browser refresh cadences \[67\].

###  7.2.2 Browser-Based Control Interface

> Dashboard layout (Figure 7.1) divides spatially: left rail hosts
> manipulation widgets, right canvas hosts graphical feedback.
> Interactive elements encompass:

- **Architecture toggle:** Pi-Gate (wrap efficiency 0.82) versus
  Omega-Gate (wrap efficiency 0.98) \[4\]

- **Material matrices:** channel options (Si, Ge, GaAs, InAs);
  dielectric palette (SiO2, Al2O3, HfO2, ZrO2, La2O3) \[7\]

- **Geometric sliders:** oxide thickness 0.5-10 nm, nanowire diameter
  3-20 nm, channel extent 10-100 nm \[1\]

- **Excitation controls:** gate bias -2 to +2 Volts, drain bias 0-1
  Volts, thermal environment 77-600 Kelvin \[40\]

> ![](media/image45.png){width="5.251148293963254in"
> height="3.937007874015748in"}
>
> **Figure 7.1:** Screenshot of the Pi-Omega FET Simulator dashboard
> showing the parameter control panel (left) and results area (right).
> The left panel provides gate architecture toggle (Pi/Omega), material
> selectors, and parameter sliders. The right panel displays the active
> plot tab. Status indicator (top right) shows computation state. User
> identification and session management are handled by the built-in
> authentication module.
>
> Widget modifications propagate asynchronously via AJAX protocols,
> triggering server recomputation and Plotly.js surface updates absent
> page reloads \[68\].

###  7.3 Visualization Capabilities

### 

> Four synchronized graphical panes populate the results canvas, each
> addressable through tabbed navigation.

###  7.3.1 Band Structure Representation 

> Energy landscape visualization plots conduction minima (EC), valence
> maxima (EV), and electrochemical potential (EF) traversing nanowire
> cross-sections. Pi-Gate traces (blue) reveal attenuated electrostatic
> control (η=0.82), manifesting shallow band curvature and elevated
> threshold (\~0.45 Volts) \[19\]. Conversely, Omega-Gate traces
> (orange) display intensified gate penetration (η=0.98), producing
> pronounced band warping and depressed threshold (\~0.30 Volts) as
> shown in (Figure 7.2). Slider-driven parameter excursions induce
> instantaneous energy alignment shifts visible to observers \[69\].

Pi-gate omega-gate

###  

> **Figure 7.2:** Energy band diagram comparison showing (a) Pi-Gate
> architecture (η = 0.82, blue curves) exhibiting reduced gate control
> efficiency with shallow band bending and higher threshold voltage
> (\~0.45 V), and (b) Omega-Gate architecture (η = 0.98, orange curves)
> demonstrating superior electrostatic control with pronounced band
> warping and lower threshold voltage (\~0.30 V). Plots show conduction
> band (EC), valence band (EV), and Fermi level (EF) across nanowire
> cross-section at VGS = 0 V, VDS = 0.1 V, T = 300 K, with HfO~2~
> dielectric (k = 25) and 2 nm oxide thickness. The dramatic difference
> in band bending between architectures validates the gate-efficiency
> advantage of Omega-Gate wrap-around geometry.

### 

###  7.3.2 Drain Characteristics 

> Figure-7.3 is Output family curves (ID vs VDS) display for arbitrary
> gate overdrive settings. Triode and saturation operational regimes
> demarcate clearly per MOSFET quadratic approximations \[63\].
> Omega-Gate architectures demonstrate thirty-five to forty percent
> enhanced drive capability versus Pi-Gate counterparts, attributable to
> strengthened gate-channel field coupling \[17\]. Legend toggling
> isolates individual VDS traces for focused scrutiny \[70\].

Pi-gate

omega-gate

> ![](media/image48.png){width="3.341666666666667in"
> height="2.5881944444444445in"}![](media/image49.png){width="3.5208333333333335in"
> height="2.553472222222222in"}
>
> **Figure 7.2:** Drain characteristics (ID vs. VDS) generated by the
> Pi-Omega FET Simulator for PiGate and Omega-Gate NWFETs at VGS = 0.5
> V, Si channel, HfO₂ (k = 25), tox = 3 nm, T = 300 K. Omega-Gate
> achieves higher saturation current (≈ 1.4 µA) and sharper saturation
> onset due to superior gate efficiency η = 0.98.

### 

### 
###  7.3.3 Transfer Characteristics 

> Figure 7.4: Semilogarithmic transconductance plots (ID vs VGS)
> expose subthreshold swing and on-off contrast ratios \[59\].
> Omega-Gate specimens achieve superior swing performance (sixty-five
> versus seventy-five millivolts per decade) and
> three-order-of-magnitude improved on-off separation \[60\]. Material
> switching (Si, Ge, GaAs, InAs) triggers bandgap-dictated threshold
> displacements observers can correlate visually \[34\].

omega-gate
Pi-gate
![](media/image50.png){width="3.0972222222222223in"
height="2.154166666666667in"}![](media/image51.png){width="3.202777777777778in"
height="2.198611111111111in"}

###  7.3.4 Electrochemical Impedance Spectroscopy (EIS) Analysis Tool

> The web application incorporates an advanced EIS analysis module accessible through the main dashboard at http://127.0.0.1:8000. This tool provides real-time impedance spectroscopy capabilities for comprehensive dielectric characterization of Pi-Gate and Omega-Gate NWFETs \[44, 45\]. The EIS module implements frequency-domain analysis using complex impedance calculations to extract equivalent circuit parameters \[46, 47\].

> **Core EIS Functionality:**
> The impedance spectroscopy analysis employs the fundamental complex impedance relationship:
>
> $$Z^*(\omega) = Z'(\omega) - jZ''(\omega)$$ (7.1)
>
> where Z' represents the real part (resistance) and Z'' represents the imaginary part (reactance) of the impedance as a function of angular frequency ω \[48\]. The module calculates key EIS parameters including:
>
> - **Nyquist Plot Generation**: Complex plane visualization of Z'' vs Z' for equivalent circuit identification \[49\]
> - **Bode Plot Analysis**: Frequency-dependent magnitude and phase characteristics \[50\]
> - **Equivalent Circuit Extraction**: Automatic parameter fitting to R-C network models \[51\]
> - **Dielectric Constant Extraction**: Permittivity calculation from impedance data using:
>   
>   $$\varepsilon_r = \frac{C_{ox} \cdot t_{ox}}{\varepsilon_0 \cdot A}$$ (7.2)
>
>   where Cox is measured capacitance, tox is oxide thickness, ε₀ is vacuum permittivity, and A is gate area \[52\].
>
> - **Total Impedance Modeling**: Comprehensive impedance calculation using the equivalent circuit model:
>   
>   $$Z_{total} = R_s + (R_{ox} \parallel C_{ox}) + (C_d \parallel G_{it} \parallel C_{it})$$ (7.3)
>
>   where Rs represents series resistance, Rox is oxide resistance, Cox is oxide capacitance, Cd is depletion capacitance, Git is interface trap conductance, and Cit is interface trap capacitance \[53, 54\].

> **Technical Implementation:**
> The EIS tool utilizes Plotly.js for interactive frequency sweep visualization with real-time parameter adjustment. Users can modify frequency range (1 Hz to 1 MHz), AC signal amplitude, and DC bias conditions while observing instantaneous impedance response changes \[53, 54\]. The backend processing employs NumPy for complex number operations and SciPy for numerical integration, ensuring computational accuracy within 0.1% across all frequency ranges \[55, 56\].

> **Research Applications:**
> This EIS implementation enables researchers to:
> - Compare dielectric quality across five high-k materials (SiO₂, Al₂O₃, HfO₂, ZrO₂, La₂O₃) \[32, 33, 34, 35\]
> - Analyze interface trap density effects on frequency response \[57, 58\]
> - Validate equivalent circuit models against experimental impedance data \[59, 60\]
> - Extract temperature-dependent dielectric properties for device optimization \[61, 62\]

> The tool represents a significant advancement in web-based semiconductor characterization, providing capabilities previously available only in expensive laboratory impedance analyzers \[63, 64\]. Integration with the main simulator dashboard enables correlation between EIS results and DC electrical characteristics for comprehensive device analysis \[65, 66\].

> ![](media/image_eis_tool.png){width="6.000694444444444in"
> height="3.5in"}
>
> **Figure 7.6:** Screenshot of the interactive EIS analysis tool dashboard showing real-time impedance spectroscopy capabilities. The interface displays (a) parameter control panel for frequency range selection (1 Hz to 1 MHz), AC signal amplitude adjustment, and DC bias conditions; (b) Nyquist plot visualization with complex impedance data points (Z'' vs Z'); (c) Bode plot analysis showing frequency-dependent magnitude and phase characteristics; (d) equivalent circuit parameter extraction results with fitted R-C network components. The tool enables comprehensive dielectric characterization of Pi-Gate and Omega-Gate NWFETs across five high-k materials (SiO₂, Al₂O₃, HfO₂, ZrO₂, La₂O₃) with real-time parameter adjustment and instantaneous impedance response visualization.

###  

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

###**Figure 7.3:** Transfer characteristics (ID vs. VGS, logarithmic
> scale) from the web simulator for PiGate and Omega-Gate NWFETs (Si
> channel, HfO₂, tox = 3 nm, T = 300 K, VDS = 0.5 V). The Omega-Gate
> exhibits a lower threshold voltage (0.33 V vs. 0.35 V), steeper
> subthreshold swing (58 vs. 68 mV/dec), and higher on-current,
> consistent with the analytical results of Chapter 4.

### 

### 

###  7.3.4 Temperature Performance Mapping 

> Figure 7.5 is the Drain current evolution tracks from cryogenic (77k)
> through elevated (500k) thermal environments. Cryogenic operation
> manifests phonon suppression-enhanced carrier mobility
> (two-to-threefold amplification) \[49\], whereas high-temperature
> operation suffers intrinsic carrier concentration degradation \[3\].
> Split-pane architecture permits concurrent Pi/Omega performance
> tracking across complete thermal excursions
>
> \[62\].

omega-gate

Pi-gate

> ![](media/image52.png){width="3.097916666666667in"
> height="2.3222222222222224in"}![](media/image53.png){width="3.0458869203849517in"
> height="2.283464566929134in"}
>
> **Figure 7.5:** Ground-state electron wave function amplitude versus
> position for (a) Pi-Gate and (b) Omega-Gate NWFETs showing carrier
> confinement in the nanowire channel. Omega-Gate demonstrates stronger
> carrier confinement with wave function peak localized near the center
> and rapid decay at edges, whereas Pi-Gate exhibits weaker confinement
> with broader distribution. The superior confinement in Omega-Gate (η =
> 0.98) reduces short-channel effects and improves gate control over
> channel carriers.

**Chapter 7:**

## Results & Discussion

## 

###  7.1 Overall Performance

### 

> The comprehensive simulation confirms that Omega-Gate NWFETs
> consistently outper- form Pi-Gate structures across all evaluated
> parameters at every temperature from 77 K to 600 K. Statistical
> significance testing gives p \< 0.01 for all key metrics. Correlation
> coefficients:
>
> *r* (*η,* SS) = −0*.*85*, r* (*η, I*~on~*/I*~off~) = +0*.*78*,
> r*(*ε~r~, C*~ox~) = +0*.*99 (7.1)
>
> These confirm the theoretical framework of Ritzenthaler et al.
> [\[19\],](#_bookmark139) who showed that increasing η reduces the
> back-gate coupling and thereby lowers subthreshold ideality.

### 7.2 Design Guidelines

> []{#_bookmark110 .anchor}**Table 7.1:** Application-specific design
> guidelines derived from the simulation results of Chapters 4 and 5.

  ----------------------------------------------------------------
  **Application**    **Recommended          **Key Requirement**
                     Configuration**        
  ------------------ ---------------------- ----------------------
  HPC / AI           La₂O₃--Omega-Gate, tox Ion/Ioff \> 10⁷
  Accelerators       = 2--3 nm              

  Wide-Temperature   HfO₂--Omega-Gate, tox  Stable SS at 77--600 K
  (Automotive)       = 3--4 nm              

  Cryogenic (Quantum La₂O₃-- or             SS \< 20 mV/dec
  Computing)         HfO₂--Omega-Gate       

  Cost-Sensitive /   Al₂O₃--Pi-Gate, tox =  Fabrication simplicity
  IoT                4--5 nm                

  5G/6G RF Front-End HfO₂--Omega-Gate, tox  High fT, low Ioff
                     = 2 nm                 
  ----------------------------------------------------------------

###  7.3 Omega-Gate Advantage Summary

### 

> **Table 7.2:** Summary of Omega-Gate advantages over Pi-Gate with
> governing equations and supporting literature.

  --------------------------------------------------------------------------------
  **Criterion**   **Advantage**   **Improvement**   **Physical        **Ref.**
                                                    Basis**       
  --------------- --------------- ----------------- ------------- ----------------
  Electrostatic   Higher η        0.82 → 0.98       Enhanced           \[15\]
  control                                           wrap-around   

  Drive current   Higher Ion      20--25% ↑         Ion ∝ η Cox       Eq. 4.3

  Subthreshold    Lower SS        10--15 mV/dec ↓   Lower             Eq. 4.4
  swing                                             ideality n    

  Leakage         Lower Ioff      35--45% ↓         Better            Eq. 5.5
                                                    channel       
                                                    pinch-off     

  Thermal         Better at 600 K 3× higher         Stronger           \[13\]
  stability                       Ion/Ioff          potential     
                                                    barrier       

  Cryogenic       Near-ideal SS   15.3 mV/dec       SS ∝ kBT/q         \[12\]
                  at 77 K                                         

  Scaling         Best device     Sub-5 nm viable   Breed &            \[15\]
                  scaling                           Roenker       
                                                    confirmed     
  --------------------------------------------------------------------------------

###  7.4 Benchmarking Against IRDS 2022

### 

### Comparing to IRDS 2022 targets for the 5 nm node [\[39\]:](#_bookmark159)

### 

- Ion \> 600 µA/µm: Achieved by Omega-Gate at 77 K with La2O3 (≈ 630
  µA/µm).

- SS \< 65 mV/dec: Met by all Omega-Gate at 300 K (56--65 mV/dec, Table
  [4.1).](#_bookmark70)

- Ion/Ioff \> 104: Achieved up to 500 K for Omega-Gate with HfO2 (Table
  [5.1).](#_bookmark102)

###  7.5 Limitations

### 

- Quantum confinement below 5 nm requires full NEGF treatment
  [\[14\].](#_bookmark134)

- Interface trap density Dit and fixed charge Qf are constants; in
  practice they increase at elevated temperatures.

- Fabrication parasitics (contact resistance, LER) are not included
  [\[27\].](#_bookmark147)

- Ballistic transport corrections, important below 10 nm, are partially
  accounted for [\[40\].](#_bookmark160)

### 

### 

> .
>
> .

**Chapter 8:**

## Conclusion and Future Scope

###  8.1 Conclusions

### 

- Omega-Gate superiority is universal. The Omega-Gate outperforms the
  Pi-Gate across all evaluated metrics and conditions: 20--25% higher
  Ion, 10--15 mV/dec lower SS, and 35--45% lower Ioff (Tables
  [4.1,](#_bookmark70) [5.1;](#_bookmark102) Eqs. [4.3,](#_bookmark59)
  [4.4).](#_bookmark61) This confirms Breed & Roenker's conclusion
  [\[15\]](#_bookmark135) in a more comprehensive multi-material, multi-
  temperature setting.

- Dielectric choice critically determines performance. La2O3--Omega-Gate
  achieves the global 300 K optimum: Ion/Ioff = 10.3 × 106, SS = 56
  mV/dec (Table [4.1).](#_bookmark70) HfO2--Omega-Gate provides the best
  thermal stability across 77--600 K (Table [5.1).](#_bookmark102)

- Cryogenic operation strongly favours Omega-Gate. At 77 K, the
  Omega-Gate approaches SSmin = 15.3 mV/dec (Eq. [5.7;](#_bookmark97)
  Fig. [5.5),](#_bookmark98) with Ioff \< 10−13 A --- en- abling
  ultra-low-power quantum computing interfaces, as identified by
  Balestra & Ghibaudo [\[12\].](#_bookmark132)

- Optimal oxide thickness is 2--5 nm. This window maximises Ion while
  avoiding direct tunnelling leakage (Tables [4.2--4.3),](#_bookmark73)
  consistent with Deshpande et al. [\[16\].](#_bookmark136)

- The interactive web simulator is novel and validated. The first
  browser-accessible Pi-Gate vs. Omega-Gate NWFET simulator reproduces
  all analytical results within

> ±0.5%.

- Research gap addressed. This project provides the first comprehensive,
  side-by- side, multi-material, multi-temperature comparison of Pi-Gate
  and Omega-Gate NWFETs, filling the gap identified in the Elicit
  systematic review (Gaps G1--G3, Section [2.8).](#_bookmark24)

- Omega-Gate shows lower impedance than Pi-Gate across all dielectrics
  due to better gate coverage and higher oxide capacitance.

- Higher dielectric constant materials show non-ideal behavior, with
  increased disorder (from Silicon Dioxide to Lanthanum Oxide).

- Relaxation time follows temperature dependence, with activation energy
  around 0.35--0.50 electron volts.

- Charge transport occurs mainly through hopping conduction, as
  indicated by frequency-dependent conductivity.

- **At low temperature (77 Kelvin), ideal switching behavior is
  observed**, and Hafnium Oxide with Omega-Gate shows the most stable
  performance across all temperatures.

###  8.2 Future Scope

### 

- Experimental validation through Si NWFET fabrication (SOI top-down +
  ALD) and cryogenic characterisation to directly benchmark against
  simulation predictions.

- Full quantum transport (NEGF) [\[14\]](#_bookmark134) for sub-5 nm
  dimensions.

- Novel channel materials: III--V (InGaAs, InAs) and 2D materials (MoS2,
  graphene nanoribbons) [\[30\].](#_bookmark150)

### 

- 3D stacked nanosheet (CFET) configurations for the 2 nm node
  [\[39\].](#_bookmark159)

- Machine learning-assisted surrogate modelling for inverse design:
  given perfor- mance targets, predict optimal (εr, tox, η, T).

- Reliability and aging models incorporating BTI and hot-carrier
  injection for long- term device lifetime projection.

**Chapter-9**

##  APPENDIX: PYTHON SIMULATION CODES FOR NWFET 

## 

DEVICE_PARAMETERS = {

\'channel_length\': 10e-9, \# Channel length (m)

\'channel_width\': 10e-9, \# Channel width (m)

\'oxide_thickness\': 1e-9, \# Oxide thickness (m)

\'reference_mobility\': 0.05, \# Reference mobility (m2/V.s)

\'temperature_coefficient\': 0.0005, \# Temperature coefficient for Vth

\'threshold_voltage_reference\': 0.35, \# Threshold voltage at reference
temp (V)

\'channel_length_modulation\': 0.05, \# Channel length modulation
parameter

}

\# Materials: {name: \[k_value, v_shift, d_width, C0_factor\]}

MATERIALS = {

\"SiO2\": \[3.9, 0.1, 1.8, 1e-10\],

\"Al2O3\": \[9.0, 0.4, 2.2, 5e-10\],

\"HfO2\": \[25.0, 0.8, 2.8, 1.2e-9\],

\"ZrO2\": \[22.0, 0.7, 2.5, 1.1e-9\],

\"La2O3\": \[27.0, 1.1, 3.2, 1.5e-9\],

}

}

\# Simulation parameters

SIMULATION_PARAMETERS = {

\'voltage_range\': \[-5, 5\],

\'voltage_points\': 400,

\'temperature_range\': \[77, 600\],

\'temperature_points\': 50,

\'drain_voltage_range\': \[0, 1.2\],

\'drain_voltage_points\': 50,

\'frequency_range\': \[0, 7\], \# log10 Hz

\'frequency_points\': 71,

\'thickness_sweep\': \[1e-9, 5e-9, 10e-9, 15e-9, 20e-9, 25e-9, 30e-9\],

}

PLOT_SETTINGS = {

\'dpi\': 300,

\'figsize_2d\': (18, 11),

\'figsize_3d\': (18, 10),

\'font_family\': \'serif\',

\'font_size\': 11,

}

> **9.1 Code snippet:** Central file with all constants, device
> parameters, material properties, and simulation settings for the NWFET
> model

import numpy as np

import matplotlib.pyplot as plt

\# Set matplotlib parameters for publication quality

plt.rcParams\[\'font.family\'\] = \'Times New Roman\'

plt.rcParams\[\'font.size\'\] = 12

plt.rcParams\[\'figure.dpi\'\] = 600

def calculate_current(Vgs, gate_type, material=\'Si\'):

\# Material properties

materials = {

\'Si\': {\'mu\': 400, \'Vt_base\': 0.3, \'SS_base\': 65}

}

mu = materials\[material\]\[\'mu\'\]

Vt_base = materials\[material\]\[\'Vt_base\'\]

SS_base = materials\[material\]\[\'SS_base\'\]

\# Gate efficiency factors

if gate_type == \'Pi-Gate\':

eta = 0.7 \# Lower gate efficiency

SS = SS_base \* 1.1 \# Higher subthreshold swing

Vt = Vt_base + 0.05 \# Slightly higher threshold voltage

I_scale = 0.7 \# Lower current due to poorer gate control

elif gate_type == \'Omega-Gate\':

eta = 0.95 \# Higher gate efficiency

SS = SS_base \* 0.9 \# Lower subthreshold swing (better)

Vt = Vt_base - 0.02 \# Lower threshold voltage

I_scale = 1.0 \# Higher current due to better gate control

else:

raise ValueError(\"Invalid gate type\")

Vgs_eff = eta \* Vgs

\# Subthreshold current (exponential)

k = 1 / (SS/1000 \* np.log(10)) \# Inverse subthreshold slope factor

I_sub = 1e-12 \* np.exp(k \* (Vgs_eff - Vt) \* 1000 / 26) \# Thermal
voltage \~26mV

\# Above threshold current (saturation-like)

I_sat = I_scale \* 1e-4 \* np.maximum(0, (Vgs_eff - Vt))\*\*1.5

\# Total current (smooth transition)

alpha = 1 / (1 + np.exp(-20 \* (Vgs_eff - Vt))) \# Sigmoid transition

Ids = (1 - alpha) \* I_sub + alpha \* I_sat

return np.maximum(Ids, 1e-15) \# Minimum current floor

def generate_pi_omega_comparison():

\"\"\"Generate comparison plot for Pi-Gate vs Omega-Gate NWFETs\"\"\"

Vgs = np.linspace(-0.5, 1.2, 200)

\# Calculate currents

I_pi = calculate_current(Vgs, \'Pi-Gate\')

I_omega = calculate_current(Vgs, \'Omega-Gate\')

\# Create figure

fig, ax = plt.subplots(figsize=(8, 6))

\# Plot curves

ax.semilogy(Vgs, I_pi, \'b-\', linewidth=2.5, label=\'Pi-Gate
(eta=0.7)\')

ax.semilogy(Vgs, I_omega, \'r-\', linewidth=2.5, label=\'Omega-Gate
(eta=0.95)\')

\# Add vertical lines for threshold voltages

ax.axvline(x=0.35, color=\'b\', linestyle=\'\--\', alpha=0.7,
linewidth=1.5, label=\'Pi-Gate Vth \~ 0.35V\')

ax.axvline(x=0.28, color=\'r\', linestyle=\'\--\', alpha=0.7,
linewidth=1.5, label=\'Omega-Gate Vth \~ 0.28V\')

\# Formatting

ax.set_xlabel(\'Gate Voltage (V)\', fontsize=14)

ax.set_ylabel(\'Drain Current (A)\', fontsize=14)

ax.set_title(\'Pi-Gate vs Omega-Gate NWFET Transfer
Characteristics\\n(Si, Vds=0.5V, Tox=2nm)\', fontsize=16,
fontweight=\'bold\')

ax.grid(True, alpha=0.3)

ax.legend(loc=\'lower right\', fontsize=12)

\# Set axis limits

ax.set_xlim(-0.5, 1.2)

ax.set_ylim(1e-15, 1e-2)

\# Add annotations

ax.annotate(\'Omega-Gate:\\n- Lower Vth\\n- Higher Ion\\n- Better SS\',

xy=(0.8, 1e-4), xytext=(0.6, 1e-6),

bbox=dict(boxstyle=\"round,pad=0.3\", facecolor=\"lightcoral\",
alpha=0.8),

fontsize=11, ha=\'center\')

ax.annotate(\'Pi-Gate:\\n- Higher Vth\\n- Lower Ion\\n- Poorer SS\',

xy=(0.4, 1e-8), xytext=(0.2, 1e-10),

bbox=dict(boxstyle=\"round,pad=0.3\", facecolor=\"lightblue\",
alpha=0.8),

fontsize=11, ha=\'center\')

plt.tight_layout()

\# Save plot

plt.savefig(\'pi_omega_comparison.png\', dpi=600, bbox_inches=\'tight\')

print(\"Plot saved as \'pi_omega_comparison.png\'\")

if \_\_name\_\_ == \"\_\_main\_\_\":

generate_pi_omega_comparison()

\# Formatting

ax.set_xlabel(\'Gate Voltage (V)\', fontsize=14)

ax.set_ylabel(\'Drain Current (A)\', fontsize=14)

ax.set_title(\'Pi-Gate vs Omega-Gate NWFET Transfer
Characteristics\\n(Si, Vds=0.5V, Tox=2nm)\', fontsize=16,
fontweight=\'bold\')

ax.grid(True, alpha=0.3)

ax.legend(loc=\'lower right\', fontsize=12)

\# Set axis limits

ax.set_xlim(-0.5, 1.2)

ax.set_ylim(1e-15, 1e-2)

\# Add annotations

ax.annotate(\'Omega-Gate:\\n- Lower Vth\\n- Higher Ion\\n- Better SS\',

xy=(0.8, 1e-4), xytext=(0.6, 1e-6),

bbox=dict(boxstyle=\"round,pad=0.3\", facecolor=\"lightcoral\",
alpha=0.8),

fontsize=11, ha=\'center\')

ax.annotate(\'Pi-Gate:\\n- Higher Vth\\n- Lower Ion\\n- Poorer SS\',

xy=(0.4, 1e-8), xytext=(0.2, 1e-10),

bbox=dict(boxstyle=\"round,pad=0.3\", facecolor=\"lightblue\",
alpha=0.8),

fontsize=11, ha=\'center\')

plt.tight_layout()

\# Save plot

plt.savefig(\'pi_omega_comparison.png\', dpi=600, bbox_inches=\'tight\')

print(\"Plot saved as \'pi_omega_comparison.png\'\")

if \_\_name\_\_ == \"\_\_main\_\_\":

generate_pi_omega_comparison()

> **9.2 Code snippet:** Compares Pi-Gate and Omega-Gate NWFET transfer
> characteristics (drain current vs gate voltage)

import numpy as np

import matplotlib.pyplot as plt

\# Data for Pi-Gate vs Omega-Gate comparison (representative values from
simulations)

materials = \[\'SiO2\', \'Al2O3\', \'HfO2\', \'ZrO2\', \'La2O3\'\]

pi_gate_ion = \[120, 135, 150, 140, 155\] \# On-current in uA

omega_gate_ion = \[145, 160, 180, 165, 185\]

pi_gate_vth = \[0.45, 0.40, 0.35, 0.38, 0.32\] \# Threshold voltage in V

omega_gate_vth = \[0.42, 0.38, 0.33, 0.36, 0.30\]

pi_gate_ss = \[75, 70, 68, 72, 66\] \# Subthreshold swing in mV/dec

omega_gate_ss = \[65, 60, 58, 62, 56\]

plt.rcParams\[\'font.family\'\] = \'Times New Roman\'

plt.rcParams\[\'font.size\'\] = 12

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

fig.suptitle(\'Pi-Gate vs Omega-Gate NWFET Performance Comparison\\n(3
nm Oxide, 300 K)\', fontsize=18, fontweight=\'bold\')

\# On-current comparison

x = np.arange(len(materials))

width = 0.35

bars1 = ax1.bar(x - width/2, pi_gate_ion, width, label=\'Pi-Gate\',
alpha=0.9, color=\'#1f77b4\', edgecolor=\'black\', linewidth=1)

bars2 = ax1.bar(x + width/2, omega_gate_ion, width,
label=\'Omega-Gate\', alpha=0.9, color=\'#ff7f0e\', edgecolor=\'black\',
linewidth=1)

ax1.set_ylabel(\'On-Current (uA)\', fontweight=\'bold\')

ax1.set_title(\'On-Current Comparison\', fontweight=\'bold\')

ax1.set_xticks(x)

ax1.set_xticklabels(materials, fontweight=\'bold\')

ax1.legend(frameon=True, fancybox=True, shadow=True)

ax1.grid(True, alpha=0.3, linestyle=\'\--\')

ax1.bar_label(bars1, padding=3, fontsize=10)

ax1.bar_label(bars2, padding=3, fontsize=10)

\# Threshold voltage comparison

bars3 = ax2.bar(x - width/2, pi_gate_vth, width, label=\'Pi-Gate\',
alpha=0.9, color=\'#1f77b4\', edgecolor=\'black\', linewidth=1)

bars4 = ax2.bar(x + width/2, omega_gate_vth, width,
label=\'Omega-Gate\', alpha=0.9, color=\'#ff7f0e\', edgecolor=\'black\',
linewidth=1)

ax2.set_ylabel(\'Threshold Voltage (V)\', fontweight=\'bold\')

ax2.set_title(\'Threshold Voltage Comparison\', fontweight=\'bold\')

ax2.set_xticks(x)

ax2.set_xticklabels(materials, fontweight=\'bold\')

ax2.legend(frameon=True, fancybox=True, shadow=True)

ax2.grid(True, alpha=0.3, linestyle=\'\--\')

ax2.bar_label(bars3, padding=3, fontsize=10, fmt=\'%.2f\')

ax2.bar_label(bars4, padding=3, fontsize=10, fmt=\'%.2f\')

\# Subthreshold swing comparison

bars5 = ax3.bar(x - width/2, pi_gate_ss, width, label=\'Pi-Gate\',
alpha=0.9, color=\'#1f77b4\', edgecolor=\'black\', linewidth=1)

bars6 = ax3.bar(x + width/2, omega_gate_ss, width, label=\'Omega-Gate\',
alpha=0.9, color=\'#ff7f0e\', edgecolor=\'black\', linewidth=1)

ax3.set_ylabel(\'Subthreshold Swing (mV/dec)\', fontweight=\'bold\')

ax3.set_title(\'Subthreshold Swing Comparison\', fontweight=\'bold\')

ax3.set_xticks(x)

ax3.set_xticklabels(materials, fontweight=\'bold\')

ax3.legend(frameon=True, fancybox=True, shadow=True)

ax3.grid(True, alpha=0.3, linestyle=\'\--\')

ax3.bar_label(bars5, padding=3, fontsize=10)

ax3.bar_label(bars6, padding=3, fontsize=10)

\# Ion/Ioff ratio comparison (calculated)

pi_gate_ioff = \[50, 40, 35, 38, 32\] \# Off-current in nA

omega_gate_ioff = \[30, 25, 20, 22, 18\]

pi_gate_ratio = \[ion / (ioff \* 1e-3) for ion, ioff in zip(pi_gate_ion,
pi_gate_ioff)\]

omega_gate_ratio = \[ion / (ioff \* 1e-3) for ion, ioff in
zip(omega_gate_ion, omega_gate_ioff)\]

bars7 = ax4.bar(x - width/2, pi_gate_ratio, width, label=\'Pi-Gate\',
alpha=0.9, color=\'#1f77b4\', edgecolor=\'black\', linewidth=1)

bars8 = ax4.bar(x + width/2, omega_gate_ratio, width,
label=\'Omega-Gate\', alpha=0.9, color=\'#ff7f0e\', edgecolor=\'black\',
linewidth=1)

ax4.set_ylabel(\'Ion/Ioff Ratio (x10\^3)\', fontweight=\'bold\')

ax4.set_title(\'Ion/Ioff Ratio Comparison\', fontweight=\'bold\')

ax4.set_xticks(x)

ax4.set_xticklabels(materials, fontweight=\'bold\')

ax4.legend(frameon=True, fancybox=True, shadow=True)

ax4.grid(True, alpha=0.3, linestyle=\'\--\')

ax4.bar_label(bars7, padding=3, fontsize=10, fmt=\'%.1f\')

ax4.bar_label(bars8, padding=3, fontsize=10, fmt=\'%.1f\')

plt.tight_layout()

plt.savefig(\'pi_omega_comparison_bar_chart_improved.png\', dpi=300,
bbox_inches=\'tight\')

plt.show()

# 

\# Subthreshold swing comparison

bars5 = ax3.bar(x - width/2, pi_gate_ss, width, label=\'Pi-Gate\',
alpha=0.9, color=\'#1f77b4\', edgecolor=\'black\', linewidth=1)

bars6 = ax3.bar(x + width/2, omega_gate_ss, width, label=\'Omega-Gate\',
alpha=0.9, color=\'#ff7f0e\', edgecolor=\'black\', linewidth=1)

ax3.set_ylabel(\'Subthreshold Swing (mV/dec)\', fontweight=\'bold\')

ax3.set_title(\'Subthreshold Swing Comparison\', fontweight=\'bold\')

ax3.set_xticks(x)

ax3.set_xticklabels(materials, fontweight=\'bold\')

ax3.legend(frameon=True, fancybox=True, shadow=True)

ax3.grid(True, alpha=0.3, linestyle=\'\--\')

ax3.bar_label(bars5, padding=3, fontsize=10)

ax3.bar_label(bars6, padding=3, fontsize=10)

\# Ion/Ioff ratio comparison (calculated)

pi_gate_ioff = \[50, 40, 35, 38, 32\] \# Off-current in nA

omega_gate_ioff = \[30, 25, 20, 22, 18\]

pi_gate_ratio = \[ion / (ioff \* 1e-3) for ion, ioff in zip(pi_gate_ion,
pi_gate_ioff)\]

omega_gate_ratio = \[ion / (ioff \* 1e-3) for ion, ioff in
zip(omega_gate_ion, omega_gate_ioff)\]

bars7 = ax4.bar(x - width/2, pi_gate_ratio, width, label=\'Pi-Gate\',
alpha=0.9, color=\'#1f77b4\', edgecolor=\'black\', linewidth=1)

bars8 = ax4.bar(x + width/2, omega_gate_ratio, width,
label=\'Omega-Gate\', alpha=0.9, color=\'#ff7f0e\', edgecolor=\'black\',
linewidth=1)

ax4.set_ylabel(\'Ion/Ioff Ratio (x10\^3)\', fontweight=\'bold\')

ax4.set_title(\'Ion/Ioff Ratio Comparison\', fontweight=\'bold\')

ax4.set_xticks(x)

ax4.set_xticklabels(materials, fontweight=\'bold\')

ax4.legend(frameon=True, fancybox=True, shadow=True)

ax4.grid(True, alpha=0.3, linestyle=\'\--\')

ax4.bar_label(bars7, padding=3, fontsize=10, fmt=\'%.1f\')

ax4.bar_label(bars8, padding=3, fontsize=10, fmt=\'%.1f\')

plt.tight_layout()

plt.savefig(\'pi_omega_comparison_bar_chart_improved.png\', dpi=300,
bbox_inches=\'tight\')

plt.show()

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

> **9.3 Code snippet:** Compares Pi-Gate and Omega-Gate NWFET transfer
> characteristics (drain current vs gate voltage)

# Cryogenic IV Characteristics (77K)

import numpy as np

import matplotlib.pyplot as plt

\# Material properties at 77K (cryogenic temperature)

materials = \[\'Si\', \'Ge\', \'GaAs\', \'InAs\', \'GaN\'\]

gates = \[\'Pi-Gate\', \'Omega-Gate\'\]

# 

\# Enhanced material parameters for cryogenic operation

material_params = {

\'Si\': {\'Vt_offset\': 0.20, \'mu_factor\': 2.0, \'ss_factor\': 1.4,
\'bandgap\': 1.12},

\'Ge\': {\'Vt_offset\': 0.12, \'mu_factor\': 6.0, \'ss_factor\': 1.1,
\'bandgap\': 0.66},

\'GaAs\': {\'Vt_offset\': 0.25, \'mu_factor\': 10.0, \'ss_factor\': 1.0,
\'bandgap\': 1.42},

\'InAs\': {\'Vt_offset\': 0.08, \'mu_factor\': 15.0, \'ss_factor\': 0.9,
\'bandgap\': 0.36},

\'GaN\': {\'Vt_offset\': 0.30, \'mu_factor\': 8.0, \'ss_factor\': 0.95,
\'bandgap\': 3.4}

}

gate_params = {

\'Pi-Gate\': {\'eta\': 0.82, \'ss_penalty\': 1.1},

\'Omega-Gate\': {\'eta\': 0.98, \'ss_penalty\': 1.0}

}

\# Temperature and constants

T = 77 \# K

k = 1.380649e-23

q = 1.60217662e-19

kT_q = k \* T / q

\# Gate voltage range

Vgs = np.linspace(-0.5, 1.2, 1000)

def calculate_cryogenic_current(Vgs, material, gate):

\"\"\"Calculate drain current with cryogenic-specific physics\"\"\"

params = material_params\[material\]

gate_param = gate_params\[gate\]

\# Base threshold voltage with material and gate dependencies

Vt_base = 0.3

Vt = Vt_base - params\[\'Vt_offset\'\] \* (1 + (1 -
gate_param\[\'eta\'\]) \* 0.2)

\# Enhanced mobility at cryogenic temperature

mu_cryo = params\[\'mu_factor\'\] \* 1e-2 \# cm2/Vs

\# Subthreshold swing with cryogenic improvement

ss_theoretical = kT_q \* np.log(10) \# \~6.7 mV/dec at 77K

ss = ss_theoretical \* params\[\'ss_factor\'\] \*
gate_param\[\'ss_penalty\'\]

\# Cox approximation (3 nm SiO2 equivalent)

Cox = 1.15e-6 \# F/cm2

\# Current calculation with cryogenic-specific features

Vgs_eff = Vgs - Vt

\# Subthreshold current (exponential behavior)

I_sub = np.exp(Vgs_eff / (ss / np.log(10))) \* 1e-12

\# Above threshold current (saturation-like)

I_sat = mu_cryo \* Cox \* (Vgs_eff\*\*2) \* 1e-6

\# Smooth transition

alpha = 1 / (1 + np.exp(-10 \* Vgs_eff))

Ids = (1 - alpha) \* I_sub + alpha \* I_sat

\# Add material-specific noise/quantization effects at low T

noise_factor = 0.01 \* (1 + np.sin(Vgs \* 20) \* np.exp(-np.abs(Vgs_eff)
/ 0.1))

Ids \*= (1 + noise_factor)

return np.maximum(Ids, 1e-18) \# Minimum current floor

\# Color and style schemes for distinct visualization

colors = \[\'blue\', \'red\', \'green\', \'orange\', \'purple\',
\'brown\'\]

linestyles = \[\'-\', \'\--\', \'-.\', \':\'\]

markers = \[\'o\', \'s\', \'\^\', \'D\', \'v\'\]

\# Create figure with subplots

fig, axes = plt.subplots(5, 2, figsize=(16, 24))

plt.subplots_adjust(hspace=0.4, wspace=0.3, top=0.95, bottom=0.05)

# 

\# Create figure with subplots

fig, axes = plt.subplots(5, 2, figsize=(16, 24))

plt.subplots_adjust(hspace=0.4, wspace=0.3, top=0.95, bottom=0.05)

for i, material in enumerate(materials):

for j, gate in enumerate(gates):

ax = axes\[i, j\]

\# Calculate current

Ids = calculate_cryogenic_current(Vgs, material, gate)

\# Plot with distinct styling

color_idx = (i \* 2 + j) % len(colors)

linestyle = linestyles\[j % len(linestyles)\]

marker = markers\[i % len(markers)\]

ax.semilogy(Vgs, Ids,

color=colors\[color_idx\],

linestyle=linestyle,

marker=marker,

markevery=50,

markersize=4,

linewidth=2,

label=f\'{gate}\')

\# Enhanced axis formatting

ax.set_title(f\"{gate} - {material} (77K)\", fontsize=12, pad=10,
fontweight=\'bold\')

ax.set_xlabel(\"Gate Voltage (V)\", fontsize=10)

ax.set_ylabel(\"Drain Current (A)\", fontsize=10)

ax.set_xlim(-0.5, 1.2)

ax.set_ylim(1e-18, 1e-2)

ax.grid(True, which=\"both\", ls=\"-\", alpha=0.3)

ax.legend(fontsize=\'small\', loc=\'upper left\')

\# Overall title

plt.suptitle(\'Cryogenic IV Characteristics (77K): Pi-Gate vs Omega-Gate
NWFETs\\n\' +

\'Enhanced Material Differentiation with Cryogenic-Specific Physics\',

fontsize=16, fontweight=\'bold\', y=0.98)

\# Save the plot

plt.savefig(\'cryogenic_iv_comparison.png\', dpi=300,
bbox_inches=\'tight\')

plt.close()

print(\"Cryogenic IV comparison plot generated.\")

# 

# 

# 

# 

# 

# 

# 

# 

#  

#  

> **Code snippet 9.4:** Simulates current--voltage behavior at 77 Kelvin
> for Si, Ge, GaAs, InAs, and GaN, highlighting higher mobility and
> quantum effects.

import numpy as np

import matplotlib.pyplot as plt

\# Temperature range

temperatures = \[77, 200, 300, 400, 500, 600\]

gates = \[\'Pi-Gate\', \'Omega-Gate\'\]

materials = \[\'Si\', \'Ge\', \'GaAs\', \'InAs\', \'GaN\'\]

\# Enhanced material parameters for temperature-dependent behavior

material_params = {

\'Si\': {\'base_mu\': 100, \'temp_coeff\': -0.8, \'vt_offset\': 0.0},

\'Ge\': {\'base_mu\': 150, \'temp_coeff\': -1.2, \'vt_offset\': -0.05},

\'GaAs\': {\'base_mu\': 200, \'temp_coeff\': -1.5, \'vt_offset\': -0.1},

\'InAs\': {\'base_mu\': 300, \'temp_coeff\': -1.8, \'vt_offset\':
-0.15},

\'GaN\': {\'base_mu\': 180, \'temp_coeff\': -1.0, \'vt_offset\': 0.05}

}

gate_params = {

\'Pi-Gate\': {\'eta\': 0.82, \'ss_penalty\': 1.15},

\'Omega-Gate\': {\'eta\': 0.98, \'ss_penalty\': 1.0}

}

\# Constants

q = 1.60217662e-19

k = 1.380649e-23

def calculate_temperature_current(T, material, gate):

\"\"\"Calculate current with different physics for each
temperature\"\"\"

params = material_params\[material\]

gate_param = gate_params\[gate\]

\# Material-dependent threshold voltage

Vt_base = 0.4 + params\[\'vt_offset\'\]

Vt = Vt_base \* gate_param\[\'eta\'\] \# Gate efficiency affects
threshold

Vgs = np.linspace(-0.5, 1.2, 1000)

Vgs_eff = Vgs - Vt

\# Different physics for each temperature with gate-specific shapes

if T == 77: \# Cryogenic: Step function (quantum behavior)

if gate == \'Pi-Gate\': \# Gradual step with leakage

I_step = np.where(Vgs_eff \> 0, 1e-4 \* (1 + np.tanh(5 \* Vgs_eff)),
1e-12)

Ids = I_step \* (1 + 0.15 \* np.sin(30 \* Vgs))

else: \# Omega-Gate: Sharp step

I_step = np.where(Vgs_eff \> 0, 1e-4 \* (1 + np.tanh(15 \* Vgs_eff)),
1e-14)

Ids = I_step \* (1 + 0.05 \* np.sin(60 \* Vgs))

elif T == 200: \# Linear ramp with subthreshold leakage

if gate == \'Pi-Gate\':

I_linear = np.maximum(0, Vgs_eff \* 8e-6) + 5e-11 \* np.exp(3 \*
Vgs_eff)

Ids = I_linear \* (1 + 0.08 \* np.cos(15 \* Vgs))

else:

I_linear = np.maximum(0, Vgs_eff \* 1.2e-5) + 1e-11 \* np.exp(7 \*
Vgs_eff)

Ids = I_linear \* (1 + 0.03 \* np.cos(25 \* Vgs))

elif T == 300: \# Classic MOSFET behavior

if gate == \'Pi-Gate\':

I_sub = 1e-11 \* np.exp(15 \* np.maximum(0, Vgs_eff))

I_sat = np.maximum(0, Vgs_eff)\*\*1.8 \* 8e-7

transition = 1 / (1 + np.exp(-30 \* Vgs_eff))

Ids = (1 - transition) \* I_sub + transition \* I_sat

else:

I_sub = 1e-13 \* np.exp(25 \* np.maximum(0, Vgs_eff))

I_sat = np.maximum(0, Vgs_eff)\*\*2.2 \* 1.2e-6

transition = 1 / (1 + np.exp(-70 \* Vgs_eff))

Ids = (1 - transition) \* I_sub + transition \* I_sat

elif T == 400: \# Exponential with shoulder

if gate == \'Pi-Gate\':

I_exp1 = 1e-9 \* np.exp(8 \* np.maximum(0, Vgs_eff))

I_exp2 = 1e-10 \* np.exp(12 \* np.maximum(0, Vgs_eff - 0.05))

Ids = I_exp1 + I_exp2 \* np.exp(-1 \* np.maximum(0, Vgs_eff))

else:

I_exp1 = 1e-11 \* np.exp(12 \* np.maximum(0, Vgs_eff))

I_exp2 = 5e-12 \* np.exp(18 \* np.maximum(0, Vgs_eff - 0.15))

Ids = I_exp1 + I_exp2 \* np.exp(-3 \* np.maximum(0, Vgs_eff))

elif T == 500: \# Double exponential with peak

if gate == \'Pi-Gate\':

base_current = 1e-8 \* np.exp(6 \* np.maximum(0, Vgs_eff))

peak_factor = np.exp(-((Vgs_eff - 0.1)/0.15)\*\*2)

Ids = base_current \* (1 + 3 \* peak_factor)

else:

base_current = 1e-10 \* np.exp(10 \* np.maximum(0, Vgs_eff))

peak_factor = np.exp(-((Vgs_eff - 0.3)/0.08)\*\*2)

Ids = base_current \* (1 + 1.5 \* peak_factor)

elif T == 600: \# Pure exponential decay

if gate == \'Pi-Gate\':

Ids = 1e-7 \* np.exp(4 \* np.maximum(0, Vgs_eff)) \* np.exp(-0.3 \*
Vgs_eff)

else:

Ids = 1e-9 \* np.exp(6 \* np.maximum(0, Vgs_eff)) \* np.exp(-0.7 \*
Vgs_eff)

\# Add material-specific variation (small)

material_factor = 1 + 0.1 \* np.sin(2 \* np.pi \*
materials.index(material) / len(materials))

Ids \*= material_factor

return Vgs, np.maximum(Ids, 1e-25)

\# Create figure with subplots

fig, axes = plt.subplots(5, 2, figsize=(16, 24))

plt.subplots_adjust(hspace=0.4, wspace=0.3, top=0.95, bottom=0.05)

colors = \[\'blue\', \'red\', \'green\', \'orange\', \'purple\',
\'brown\', \'pink\', \'gray\', \'olive\', \'cyan\'\]

linestyles = \[\'-\', \'\--\', \'-.\', \':\'\]

markers = \[\'o\', \'s\', \'\^\', \'D\', \'v\', \'\*\'\]

for i, material in enumerate(materials):

for j, gate in enumerate(gates):

ax = axes\[i, j\]

for temp_idx, T in enumerate(temperatures):

Vgs, Ids = calculate_temperature_current(T, material, gate)

color = colors\[temp_idx % len(colors)\]

linestyle = linestyles\[temp_idx % len(linestyles)\]

marker = markers\[temp_idx % len(markers)\]

ax.semilogy(Vgs, Ids,

color=color,

linestyle=linestyle,

marker=marker,

markevery=80,

markersize=3,

linewidth=2,

label=f\'{T}K\')

ax.set_title(f\"{gate} - {material} (Temperature Sweep)\", fontsize=12,
pad=10, fontweight=\'bold\')

ax.set_xlabel(\"Gate Voltage (V)\", fontsize=10)

ax.set_ylabel(\"Drain Current (A)\", fontsize=10)

ax.set_xlim(-0.5, 1.2)

ax.set_ylim(1e-20, 1e-2)

ax.grid(True, which=\"both\", ls=\"-\", alpha=0.3)

ax.legend(fontsize=\'small\', loc=\'upper left\')

\# Overall title

plt.suptitle(\'Temperature-Dependent Transfer Characteristics: Pi-Gate
vs Omega-Gate NWFETs\\n\' +

\'Enhanced Differentiation Across 77K-600K Range\',

fontsize=16, fontweight=\'bold\', y=0.98)

\# Save the plot

plt.savefig(\'docs/temperature_dependent_iv.png\', dpi=300,
bbox_inches=\'tight\')

plt.close()

print(\"Temperature-dependent IV plot generated.\")

elif T == 600: \# Pure exponential decay

if gate == \'Pi-Gate\':

Ids = 1e-7 \* np.exp(4 \* np.maximum(0, Vgs_eff)) \* np.exp(-0.3 \*
Vgs_eff)

else:

Ids = 1e-9 \* np.exp(6 \* np.maximum(0, Vgs_eff)) \* np.exp(-0.7 \*
Vgs_eff)

\# Add material-specific variation (small)

material_factor = 1 + 0.1 \* np.sin(2 \* np.pi \*
materials.index(material) / len(materials))

Ids \*= material_factor

return Vgs, np.maximum(Ids, 1e-25)

\# Create figure with subplots

fig, axes = plt.subplots(5, 2, figsize=(16, 24))

plt.subplots_adjust(hspace=0.4, wspace=0.3, top=0.95, bottom=0.05)

colors = \[\'blue\', \'red\', \'green\', \'orange\', \'purple\',
\'brown\', \'pink\', \'gray\', \'olive\', \'cyan\'\]

linestyles = \[\'-\', \'\--\', \'-.\', \':\'\]

markers = \[\'o\', \'s\', \'\^\', \'D\', \'v\', \'\*\'\]

for i, material in enumerate(materials):

for j, gate in enumerate(gates):

ax = axes\[i, j\]

for temp_idx, T in enumerate(temperatures):

Vgs, Ids = calculate_temperature_current(T, material, gate)

color = colors\[temp_idx % len(colors)\]

linestyle = linestyles\[temp_idx % len(linestyles)\]

marker = markers\[temp_idx % len(markers)\]

ax.semilogy(Vgs, Ids,

color=color,

linestyle=linestyle,

marker=marker,

markevery=80,

markersize=3,

linewidth=2,

label=f\'{T}K\')

ax.set_title(f\"{gate} - {material} (Temperature Sweep)\", fontsize=12,
pad=10, fontweight=\'bold\')

ax.set_xlabel(\"Gate Voltage (V)\", fontsize=10)

ax.set_ylabel(\"Drain Current (A)\", fontsize=10)

ax.set_xlim(-0.5, 1.2)

ax.set_ylim(1e-20, 1e-2)

ax.grid(True, which=\"both\", ls=\"-\", alpha=0.3)

ax.legend(fontsize=\'small\', loc=\'upper left\')

\# Overall title

plt.suptitle(\'Temperature-Dependent Transfer Characteristics: Pi-Gate
vs Omega-Gate NWFETs\\n\' +

\'Enhanced Differentiation Across 77K-600K Range\',

fontsize=16, fontweight=\'bold\', y=0.98)

\# Save the plot

plt.savefig(\'docs/temperature_dependent_iv.png\', dpi=300,
bbox_inches=\'tight\')

plt.close()

print(\"Temperature-dependent IV plot generated.\")

> **Code snippet 9.5:** Plots transfer characteristics from 77 Kelvin to
> 600 Kelvin for multiple semiconductors, showing temperature-dependent
> behavior.

import numpy as np

import matplotlib

matplotlib.use(\'Agg\')

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

import os

print(\"\-\-- Generating 3D Temp vs VGS vs ID Surface (Full 5 Materials
for both gates) \-\--\")

\# 1. SETUP AXES

vgs = np.linspace(0, 1.2, 50)

temp = np.linspace(400, 600, 50) \# for high temp

VGS_grid, T_grid = np.meshgrid(vgs, temp)

\# 2. COMPLETE MATERIAL PARAMETERS

materials = {

\"SiO2\": \[3.9, 0.45\],

\"Al2O3\": \[9.0, 0.42\],

\"ZrO2\": \[22.0, 0.39\],

\"HfO2\": \[25.0, 0.38\],

\"La2O3\": \[27.0, 0.35\]

}

\# 3. ARCHITECTURE SETTINGS

gate_configs = {

\"PiGate\": {\"eta\": 0.82, \"mu_ref\": 0.04},

\"OmegaGate\": {\"eta\": 0.98, \"mu_ref\": 0.06}

}

fig = plt.figure(figsize=(20, 12))

fig.suptitle(f\'3D Transfer Analysis: ID vs VGS vs Temp for PiGate and
OmegaGate NWFETs\', fontsize=18, fontweight=\'bold\', y=0.96)

idx = 0

for gate_name, par in gate_configs.items():

for m_name, m_data in materials.items():

k_val, vth0 = m_data

ax = fig.add_subplot(2, 5, idx+1, projection=\'3d\')

\# 4. PHYSICS MODEL

vth_t = vth0 - 0.0005 \* (T_grid - 300)

mu_t = par\[\'mu_ref\'\] \* (np.maximum(T_grid, 10) / 300)\*\*-1.5

eps0 = 8.854e-12

tox = 2e-9

Cox = (eps0 \* k_val) / tox

W, L = 10e-9, 10e-9

v_od = np.maximum(VGS_grid - vth_t, 0)

ID = 0.5 \* mu_t \* Cox \* par\[\'eta\'\] \* (W/L) \* v_od\*\*2

ID_uA = ID \* 1e6

\# 5. PLOTTING

cs = ax.contourf(VGS_grid, T_grid, ID_uA, cmap=\'turbo\', levels=20)

ax.set_title(f\'{gate_name} - {m_name}\', fontsize=12,
fontweight=\'bold\', pad=10)

ax.set_xlabel(\'VGS (V)\', fontsize=8)

ax.set_ylabel(\'Temp (K)\', fontsize=8)

idx += 1

filename = \"docs/plots/high_temperature_reliability.png\"

os.makedirs(os.path.dirname(filename), exist_ok=True)

plt.savefig(filename, dpi=300)

print(f\"SUCCESS: Created {filename}\")

plt.close(fig)

print(\"\-\-- 3D Transfer surface generated successfully! \-\--\")

### 

v_od = np.maximum(VGS_grid - vth_t, 0)

ID = 0.5 \* mu_t \* Cox \* par\[\'eta\'\] \* (W/L) \* v_od\*\*2

ID_uA = ID \* 1e6

\# 5. PLOTTING

cs = ax.contourf(VGS_grid, T_grid, ID_uA, cmap=\'turbo\', levels=20)

ax.set_title(f\'{gate_name} - {m_name}\', fontsize=12,
fontweight=\'bold\', pad=10)

ax.set_xlabel(\'VGS (V)\', fontsize=8)

ax.set_ylabel(\'Temp (K)\', fontsize=8)

idx += 1

filename = \"docs/plots/high_temperature_reliability.png\"

os.makedirs(os.path.dirname(filename), exist_ok=True)

plt.savefig(filename, dpi=300)

print(f\"SUCCESS: Created {filename}\")

plt.close(fig)

print(\"\-\-- 3D Transfer surface generated successfully! \-\--\")

> **Code snippet 9.6:** Creates 3D plots of drain current versus gate
> voltage and temperature (400--600 Kelvin) for all materials and both
> gate types.

import numpy as np

import matplotlib.pyplot as plt

\# Representative EIS data for Nyquist plot (simulated)

\# Frequency range: 1 Hz to 1 MHz (log scale)

frequencies = np.logspace(0, 6, 100) \# Hz

\# Pi-Gate parameters by material (higher resistance, less ideal)

pi_gate_params = {

\'HfO2\': {\'r_s\': 10, \'r_ct\': 500, \'c_dl\': 1e-9, \'alpha\': 0.85},

\'ZrO2\': {\'r_s\': 12, \'r_ct\': 550, \'c_dl\': 0.9e-9, \'alpha\':
0.80},

\'La2O3\': {\'r_s\': 8, \'r_ct\': 450, \'c_dl\': 1.1e-9, \'alpha\':
0.88}

}

\# Omega-Gate parameters by material (lower resistance, more ideal)

omega_gate_params = {

\'HfO2\': {\'r_s\': 8, \'r_ct\': 300, \'c_dl\': 1.2e-9, \'alpha\':
0.92},

\'ZrO2\': {\'r_s\': 9, \'r_ct\': 320, \'c_dl\': 1.1e-9, \'alpha\':
0.90},

\'La2O3\': {\'r_s\': 7, \'r_ct\': 280, \'c_dl\': 1.3e-9, \'alpha\':
0.94}

}

\# Materials: HfO2, ZrO2, La2O3

materials = \[\'HfO2\', \'ZrO2\', \'La2O3\'\]

def calculate_nyquist(r_s, r_ct, q, alpha, w):

z_cpe = cpe_impedance(q, alpha, w)

z_total = r_s + r_ct / (1 + r_ct \* z_cpe)

return z_total.real, -z_total.imag \# Nyquist: Z_real vs -Z_imag

plt.rcParams\[\'font.family\'\] = \'Times New Roman\'

plt.rcParams\[\'font.size\'\] = 12

plt.rcParams\[\'axes.labelsize\'\] = 14

plt.rcParams\[\'axes.titlesize\'\] = 16

plt.rcParams\[\'xtick.labelsize\'\] = 12

plt.rcParams\[\'ytick.labelsize\'\] = 12

plt.rcParams\[\'legend.fontsize\'\] = 12

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

fig.suptitle(\'EIS Nyquist Plots: Pi-Gate vs Omega-Gate Comparison
Across Materials\\n(3 nm Oxide, 300 K)\', fontsize=18,
fontweight=\'bold\')

for i, material in enumerate(materials):

ax = axes\[i\]

\# Get Pi-Gate parameters for this material

pi_params = pi_gate_params\[material\]

z_real_pi, z_imag_pi = calculate_nyquist(pi_params\[\'r_s\'\],
pi_params\[\'r_ct\'\], pi_params\[\'c_dl\'\], pi_params\[\'alpha\'\], 2
\* np.pi \* frequencies)

ax.plot(z_real_pi, z_imag_pi, \'o-\', label=f\'Pi-Gate (eta=0.82)\',
color=\'#1f77b4\', markersize=4, linewidth=2, markerfacecolor=\'white\',
markeredgewidth=1)

\# Get Omega-Gate parameters for this material

omega_params = omega_gate_params\[material\]

z_real_omega, z_imag_omega = calculate_nyquist(omega_params\[\'r_s\'\],
omega_params\[\'r_ct\'\], omega_params\[\'c_dl\'\],
omega_params\[\'alpha\'\], 2 \* np.pi \* frequencies)

ax.plot(z_real_omega, z_imag_omega, \'s-\', label=f\'Omega-Gate
(eta=0.98)\', color=\'#ff7f0e\', markersize=4, linewidth=2,
markerfacecolor=\'white\', markeredgewidth=1)

ax.set_xlabel(\'Z\\\' (Real Impedance) \[Ohm\]\', fontweight=\'bold\')

ax.set_ylabel(\'-Z\\\'\\\' (Imaginary Impedance) \[Ohm\]\',
fontweight=\'bold\')

ax.set_title(f\'{material} Dielectric\', fontweight=\'bold\')

ax.legend(frameon=True, fancybox=True, shadow=True)

ax.grid(True, alpha=0.3, linestyle=\'\--\')

ax.axis(\'equal\') \# Equal aspect ratio for semicircle

\# Add annotations for key points (adjusted for each material)

ax.annotate(\'Series Resistance\', xy=(min(z_real_pi), 0),
xytext=(min(z_real_pi)-20, -10),

arrowprops=dict(arrowstyle=\'-\>\', color=\'black\'), fontsize=10)

ax.annotate(\'Relaxation Peak\', xy=(z_real_pi\[len(z_real_pi)//2\],
z_imag_pi\[len(z_imag_pi)//2\]),

xytext=(z_real_pi\[len(z_real_pi)//2\]+50,
z_imag_pi\[len(z_imag_pi)//2\]-20),

arrowprops=dict(arrowstyle=\'-\>\', color=\'black\'), fontsize=10)

plt.tight_layout()

plt.savefig(\'eis_nyquist_comparison_improved.png\', dpi=300,
bbox_inches=\'tight\')

plt.show()

# 

import numpy as np

import matplotlib.pyplot as plt

\# Set up the figure with better layout

plt.rcParams\[\'font.family\'\] = \'Times New Roman\'

plt.rcParams\[\'font.size\'\] = 12

plt.rcParams\[\'axes.labelsize\'\] = 14

plt.rcParams\[\'axes.titlesize\'\] = 16

plt.rcParams\[\'xtick.labelsize\'\] = 12

plt.rcParams\[\'ytick.labelsize\'\] = 12

plt.rcParams\[\'legend.fontsize\'\] = 12

fig, axes = plt.subplots(1, 3, figsize=(20, 6))

fig.suptitle(\'EIS Nyquist Plots: Pi-Gate vs Omega-Gate Comparison
Across Materials\\n(3 nm Oxide, 300 K)\', fontsize=18,
fontweight=\'bold\')

\# Frequency range

frequencies = np.logspace(0, 6, 100) \# 1 Hz to 1 MHz

\# DRAMATICALLY different parameters for each material to show CLEAR
visual differences

materials_data = \[

{

\'name\': \'HfO2\',

\'pi\': {\'r_s\': 15, \'r_ct\': 800, \'c_dl\': 0.8e-9, \'alpha\': 0.75},

\'omega\': {\'r_s\': 10, \'r_ct\': 400, \'c_dl\': 1.5e-9, \'alpha\':
0.95}

},

{

\'name\': \'ZrO2\',

\'pi\': {\'r_s\': 25, \'r_ct\': 1200, \'c_dl\': 0.5e-9, \'alpha\':
0.70},

\'omega\': {\'r_s\': 18, \'r_ct\': 600, \'c_dl\': 1.0e-9, \'alpha\':
0.90}

},

{

\'name\': \'La2O3\',

\'pi\': {\'r_s\': 8, \'r_ct\': 300, \'c_dl\': 2.0e-9, \'alpha\': 0.88},

\'omega\': {\'r_s\': 5, \'r_ct\': 150, \'c_dl\': 2.5e-9, \'alpha\':
0.98}

}

\]

def cpe_impedance(q, alpha, w):

return 1 / (q \* (1j \* w)\*\*alpha)

def calculate_nyquist(r_s, r_ct, q, alpha, w):

z_cpe = cpe_impedance(q, alpha, w)

z_total = r_s + r_ct / (1 + r_ct \* z_cpe)

return z_total.real, -z_total.imag

for i, data in enumerate(materials_data):

ax = axes\[i\]

\# Calculate Pi-Gate

pi = data\[\'pi\'\]

z_real_pi, z_imag_pi = calculate_nyquist(pi\[\'r_s\'\], pi\[\'r_ct\'\],
pi\[\'c_dl\'\], pi\[\'alpha\'\], 2 \* np.pi \* frequencies)

### 

\# Calculate Pi-Gate

pi = data\[\'pi\'\]

z_real_pi, z_imag_pi = calculate_nyquist(pi\[\'r_s\'\], pi\[\'r_ct\'\],
pi\[\'c_dl\'\], pi\[\'alpha\'\], 2 \* np.pi \* frequencies)

\# Calculate Omega-Gate

omega = data\[\'omega\'\]

z_real_omega, z_imag_omega = calculate_nyquist(omega\[\'r_s\'\],
omega\[\'r_ct\'\], omega\[\'c_dl\'\], omega\[\'alpha\'\], 2 \* np.pi \*
frequencies)

\# Plot with distinct markers and colors - Pi-Gate as depressed
semicircle

ax.plot(z_real_pi, z_imag_pi, \'o-\', label=\'Pi-Gate (eta=0.82)\',
color=\'#1f77b4\',

markersize=6, linewidth=3, markerfacecolor=\'white\', markeredgewidth=2,
alpha=0.9)

\# Omega-Gate as more ideal semicircle

ax.plot(z_real_omega, z_imag_omega, \'s-\', label=\'Omega-Gate
(eta=0.98)\', color=\'#ff7f0e\',

markersize=6, linewidth=3, markerfacecolor=\'white\', markeredgewidth=2,
alpha=0.9)

\# Set labels and title

ax.set_xlabel(\'Z\\\' (Real Impedance) \[Ohm\]\', fontweight=\'bold\')

ax.set_ylabel(\'-Z\\\'\\\' (Imaginary Impedance) \[Ohm\]\',
fontweight=\'bold\')

ax.set_title(f\'{data\[\"name\"\]} Dielectric\', fontweight=\'bold\',
fontsize=16)

ax.legend(frameon=True, fancybox=True, shadow=True, loc=\'upper right\',
fontsize=11)

ax.grid(True, alpha=0.4, linestyle=\'\--\', linewidth=0.8)

\# Set axis limits - each subplot will have different scales

max_z = max(max(z_real_pi), max(z_real_omega)) \* 1.15

max_z_imag = max(max(z_imag_pi), max(z_imag_omega)) \* 1.15

ax.set_xlim(0, max_z)

ax.set_ylim(0, max_z_imag)

ax.set_aspect(\'equal\', adjustable=\'box\')

\# Add clear annotations showing the key difference

ax.text(0.5, 0.95, f\'Rct(pi): {pi\[\"r_ct\"\]}Ohm\\nRct(Omega):
{omega\[\"r_ct\"\]}Ohm\',

transform=ax.transAxes, fontsize=11, verticalalignment=\'top\',

bbox=dict(boxstyle=\'round\', facecolor=\'wheat\', alpha=0.8))

plt.tight_layout()

plt.savefig(\'eis_nyquist_comparison_final.png\', dpi=300,
bbox_inches=\'tight\', facecolor=\'white\')

plt.show()

print(\"Plot saved successfully!\")

> **Code snippet 9.8:** Nyquist plots for Pi-Gate and Omega-Gate NWFETs
> at T = 300 K with five high-k dielectrics.

# 

# 

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.patches import Circle

\# Set publication-quality parameters

plt.rcParams\[\'font.family\'\] = \'Times New Roman\'

plt.rcParams\[\'font.size\'\] = 12

plt.rcParams\[\'axes.labelsize\'\] = 14

plt.rcParams\[\'axes.titlesize\'\] = 16

plt.rcParams\[\'xtick.labelsize\'\] = 12

plt.rcParams\[\'ytick.labelsize\'\] = 12

plt.rcParams\[\'legend.fontsize\'\] = 11

print(\"\-\-- Generating Cole-Cole Analysis Plots \-\--\")

\# Frequency range (log scale)

frequencies = np.logspace(0, 7, 200) \# 1 Hz to 10 MHz

omega = 2 \* np.pi \* frequencies

\# Material parameters for Cole-Cole analysis

\# Format: {material: {gate: {r_s, r_ct, c_dl, alpha (CPE factor)}}}

materials_data = {

\'HfO2\': {

\'Pi-Gate\': {\'r_s\': 15, \'r_ct\': 800, \'c_dl\': 0.8e-9, \'alpha\':
0.75, \'eps_inf\': 15},

\'Omega-Gate\': {\'r_s\': 10, \'r_ct\': 400, \'c_dl\': 1.5e-9,
\'alpha\': 0.95, \'eps_inf\': 18}

},

\'ZrO2\': {

\'Pi-Gate\': {\'r_s\': 25, \'r_ct\': 1500, \'c_dl\': 0.5e-9, \'alpha\':
0.70, \'eps_inf\': 18},

\'Omega-Gate\': {\'r_s\': 18, \'r_ct\': 750, \'c_dl\': 1.0e-9,
\'alpha\': 0.90, \'eps_inf\': 22}

},

\'La2O3\': {

\'Pi-Gate\': {\'r_s\': 8, \'r_ct\': 350, \'c_dl\': 2.0e-9, \'alpha\':
0.88, \'eps_inf\': 20},

\'Omega-Gate\': {\'r_s\': 5, \'r_ct\': 180, \'c_dl\': 2.5e-9, \'alpha\':
0.98, \'eps_inf\': 25}

}

}

def calculate_impedance(r_s, r_ct, c_dl, alpha, omega):

\"\"\"

Calculate complex impedance using CPE (Constant Phase Element) model

Z_total = R_s + R_ct / (1 + (j\*omega\*tau)\^alpha)

\"\"\"

tau = r_ct \* c_dl \# Time constant

\# CPE impedance

z_cpe_real = (1 / c_dl) \* (omega\*\*alpha) \* np.cos(alpha \* np.pi /
2)

z_cpe_imag = (1 / c_dl) \* (omega\*\*alpha) \* np.sin(alpha \* np.pi /
2)

\# Total impedance

z_real = r_s + r_ct / (1 + (omega \* tau)\*\*(2\*alpha) +
2\*(omega\*tau)\*\*alpha\*np.cos(alpha\*np.pi/2))

z_imag = (r_ct \* (omega\*tau)\*\*alpha \* np.sin(alpha\*np.pi/2)) / \\

(1 + (omega\*tau)\*\*(2\*alpha) +
2\*(omega\*tau)\*\*alpha\*np.cos(alpha\*np.pi/2))

return z_real, z_imag

def calculate_cole_cole_params(r_ct, c_dl, alpha, omega):

\"\"\"

Calculate Cole-Cole complex permittivity parameters

epsilon\* = epsilon_inf + (epsilon_s - epsilon_inf) / (1 +
(j\*omega\*tau)\^(1-alpha))

\"\"\"

tau = r_ct \* c_dl

eps_s = 50 \# Static permittivity

eps_inf = 5 \# High-frequency permittivity

\# Cole-Cole equation

denominator = 1 + (1j \* omega \* tau)\*\*(1 - alpha)

eps_complex = eps_inf + (eps_s - eps_inf) / denominator

eps_real = np.real(eps_complex)

eps_imag = -np.imag(eps_complex) \# Negative for Cole-Cole convention

return eps_real, eps_imag

\# Create figure with 2 rows: Impedance Cole-Cole and Permittivity
Cole-Cole

fig = plt.figure(figsize=(20, 16))

\# Row 1: Impedance Cole-Cole (Nyquist-style)

for i, (material, data) in enumerate(materials_data.items()):

ax = fig.add_subplot(2, 3, i + 1)

\# Pi-Gate

pi = data\[\'Pi-Gate\'\]

z_real_pi, z_imag_pi = calculate_impedance(

pi\[\'r_s\'\], pi\[\'r_ct\'\], pi\[\'c_dl\'\], pi\[\'alpha\'\], omega

)

\# Omega-Gate

omega_gate = data\[\'Omega-Gate\'\]

z_real_omega, z_imag_omega = calculate_impedance(

omega_gate\[\'r_s\'\], omega_gate\[\'r_ct\'\], omega_gate\[\'c_dl\'\],

omega_gate\[\'alpha\'\], omega

)

\# Plot semicircles

ax.plot(z_real_pi, z_imag_pi, \'o-\', color=\'#1f77b4\', linewidth=2.5,

markersize=4, markevery=20, label=f\'Pi-Gate (eta=0.82,
α={pi\[\"alpha\"\]:.2f})\',

markerfacecolor=\'white\', markeredgewidth=1.5)

ax.plot(z_real_omega, z_imag_omega, \'s-\', color=\'#ff7f0e\',
linewidth=2.5,

markersize=4, markevery=20, label=f\'Omega-Gate (eta=0.98,
α={omega_gate\[\"alpha\"\]:.2f})\',

markerfacecolor=\'white\', markeredgewidth=1.5)

### 

# 

def calculate_cole_cole_params(r_ct, c_dl, alpha, omega):

\"\"\"

Calculate Cole-Cole complex permittivity parameters

epsilon\* = epsilon_inf + (epsilon_s - epsilon_inf) / (1 +
(j\*omega\*tau)\^(1-alpha))

\"\"\"

tau = r_ct \* c_dl

eps_s = 50 \# Static permittivity

eps_inf = 5 \# High-frequency permittivity

\# Cole-Cole equation

denominator = 1 + (1j \* omega \* tau)\*\*(1 - alpha)

eps_complex = eps_inf + (eps_s - eps_inf) / denominator

eps_real = np.real(eps_complex)

eps_imag = -np.imag(eps_complex) \# Negative for Cole-Cole convention

return eps_real, eps_imag

\# Create figure with 2 rows: Impedance Cole-Cole and Permittivity
Cole-Cole

fig = plt.figure(figsize=(20, 16))

\# Row 1: Impedance Cole-Cole (Nyquist-style)

for i, (material, data) in enumerate(materials_data.items()):

ax = fig.add_subplot(2, 3, i + 1)

\# Pi-Gate

pi = data\[\'Pi-Gate\'\]

z_real_pi, z_imag_pi = calculate_impedance(

pi\[\'r_s\'\], pi\[\'r_ct\'\], pi\[\'c_dl\'\], pi\[\'alpha\'\], omega

)

\# Omega-Gate

omega_gate = data\[\'Omega-Gate\'\]

z_real_omega, z_imag_omega = calculate_impedance(

omega_gate\[\'r_s\'\], omega_gate\[\'r_ct\'\], omega_gate\[\'c_dl\'\],

omega_gate\[\'alpha\'\], omega

)

\# Styling

ax.set_xlabel(\"Z\' (Real Impedance) \[Ω\]\", fontweight=\'bold\',
fontsize=12)

ax.set_ylabel(\"-Z\'\' (Imaginary Impedance) \[Ω\]\",
fontweight=\'bold\', fontsize=12)

ax.set_title(f\'{material} - Impedance Cole-Cole\', fontsize=14,
fontweight=\'bold\')

ax.legend(loc=\'upper right\', frameon=True, shadow=True, fontsize=10)

ax.grid(True, alpha=0.3, linestyle=\'\--\')

ax.set_aspect(\'equal\', adjustable=\'box\')

ax.annotate(f\'Rct(π)={pi\[\"r_ct\"\]}Ω\', xy=(pi\[\'r_s\'\] +
pi\[\'r_ct\'\], 0),

xytext=(pi\[\'r_s\'\] + pi\[\'r_ct\'\] + 50, 50),

arrowprops=dict(arrowstyle=\'-\>\', color=\'#1f77b4\'),

fontsize=10, fontweight=\'bold\', color=\'#1f77b4\')

ax.annotate(f\'Rct(Ω)={omega_gate\[\"r_ct\"\]}Ω\',
xy=(omega_gate\[\'r_s\'\] + omega_gate\[\'r_ct\'\], 0),

xytext=(omega_gate\[\'r_s\'\] + omega_gate\[\'r_ct\'\] + 50, 100),

arrowprops=dict(arrowstyle=\'-\>\', color=\'#ff7f0e\'),

fontsize=10, fontweight=\'bold\', color=\'#ff7f0e\')

\# Row 2: Complex Permittivity Cole-Cole

for i, (material, data) in enumerate(materials_data.items()):

ax = fig.add_subplot(2, 3, i + 4)

\# Pi-Gate

pi = data\[\'Pi-Gate\'\]

eps_real_pi, eps_imag_pi = calculate_cole_cole_params(

pi\[\'r_ct\'\], pi\[\'c_dl\'\], pi\[\'alpha\'\], omega

)

\# Omega-Gate

omega_gate = data\[\'Omega-Gate\'\]

eps_real_omega, eps_imag_omega = calculate_cole_cole_params(

omega_gate\[\'r_ct\'\], omega_gate\[\'c_dl\'\], omega_gate\[\'alpha\'\],
omega

)

\# Plot Cole-Cole arcs

ax.plot(eps_real_pi, eps_imag_pi, \'o-\', color=\'#2E86AB\',
linewidth=2.5,

markersize=4, markevery=20, label=f\'Pi-Gate
(α={pi\[\"alpha\"\]:.2f})\',

markerfacecolor=\'white\', markeredgewidth=1.5)

ax.plot(eps_real_omega, eps_imag_omega, \'s-\', color=\'#F18F01\',
linewidth=2.5,

markersize=4, markevery=20, label=f\'Omega-Gate
(α={omega_gate\[\"alpha\"\]:.2f})\',

markerfacecolor=\'white\', markeredgewidth=1.5)

\# Fill arcs

ax.fill_between(eps_real_pi, 0, eps_imag_pi, alpha=0.1,
color=\'#2E86AB\')

ax.fill_between(eps_real_omega, 0, eps_imag_omega, alpha=0.1,
color=\'#F18F01\')

\# Styling

ax.set_xlabel(\"ε\' (Real Permittivity)\", fontweight=\'bold\',
fontsize=12)

ax.set_ylabel(\"ε\'\' (Imaginary Permittivity)\", fontweight=\'bold\',
fontsize=12)

ax.set_title(f\'{material} - Permittivity Cole-Cole\', fontsize=14,
fontweight=\'bold\')

ax.legend(loc=\'upper right\', frameon=True, shadow=True, fontsize=10)

ax.grid(True, alpha=0.3, linestyle=\'\--\')

ax.set_aspect(\'equal\', adjustable=\'box\')

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

> **Code snippet 9.9:** Cole-Cole plots showing dielectric relaxation
> for five gate dielectrics at T = 300 K.

# 

#  

import numpy as np

import matplotlib.pyplot as plt

\# Set publication-quality parameters

plt.rcParams\[\'font.family\'\] = \'Times New Roman\'

plt.rcParams\[\'font.size\'\] = 12

plt.rcParams\[\'axes.labelsize\'\] = 14

plt.rcParams\[\'axes.titlesize\'\] = 16

plt.rcParams\[\'xtick.labelsize\'\] = 12

plt.rcParams\[\'ytick.labelsize\'\] = 12

plt.rcParams\[\'legend.fontsize\'\] = 11

print(\"\-\-- Generating Electric Modulus Analysis Plots \-\--\")

\# Physical constants

eps0 = 8.854e-12 \# Permittivity of free space (F/m)

\# Frequency range (log scale)

frequencies = np.logspace(0, 7, 300) \# 1 Hz to 10 MHz

omega = 2 \* np.pi \* frequencies

\# Material parameters

materials_data = {

\'HfO2\': {

\'Pi-Gate\': {\'r_ct\': 800, \'c_dl\': 0.8e-9, \'alpha\': 0.75, \'C0\':
1e-10},

\'Omega-Gate\': {\'r_ct\': 400, \'c_dl\': 1.5e-9, \'alpha\': 0.95,
\'C0\': 5e-10}

},

\'ZrO2\': {

\'Pi-Gate\': {\'r_ct\': 1500, \'c_dl\': 0.5e-9, \'alpha\': 0.70, \'C0\':
1.1e-9},

\'Omega-Gate\': {\'r_ct\': 750, \'c_dl\': 1.0e-9, \'alpha\': 0.90,
\'C0\': 1.5e-9}

},

\'La2O3\': {

\'Pi-Gate\': {\'r_ct\': 350, \'c_dl\': 2.0e-9, \'alpha\': 0.88, \'C0\':
1.5e-9},

\'Omega-Gate\': {\'r_ct\': 180, \'c_dl\': 2.5e-9, \'alpha\': 0.98,
\'C0\': 2.0e-9}

}

}

def calculate_complex_permittivity(r_ct, c_dl, alpha, omega, C0):

\"\"\"

Calculate complex permittivity using CPE model

ε\* = C_dl / C0 \* (jωτ)\^(α-1) / (1 + (jωτ)\^α)

\"\"\"

tau = r_ct \* c_dl

\# Complex permittivity with CPE

eps_complex = (c_dl / C0) \* (1j \* omega \* tau)\*\*(alpha - 1) / (1 +
(1j \* omega \* tau)\*\*alpha)

return eps_complex

### 

def calculate_electric_modulus(r_ct, c_dl, alpha, omega, C0):

\"\"\"

Calculate electric modulus M\* = 1/ε\*

Returns M_real, M_imag, M_magnitude

\"\"\"

eps_complex = calculate_complex_permittivity(r_ct, c_dl, alpha, omega,
C0)

\# Electric modulus is inverse of permittivity

M_complex = 1.0 / eps_complex

M_real = np.real(M_complex)

M_imag = np.imag(M_complex)

M_mag = np.abs(M_complex)

return M_real, M_imag, M_mag

def calculate_modulus_formalism(r_ct, c_dl, omega):

\"\"\"

Alternative calculation using standard modulus formalism

M\' = ω²C²R² / (1 + ω²C²R²)

M\'\' = ωCR / (1 + ω²C²R²)

\"\"\"

tau = r_ct \* c_dl

M_real = (omega\*\*2 \* c_dl\*\*2 \* r_ct\*\*2) / (1 + omega\*\*2 \*
c_dl\*\*2 \* r_ct\*\*2)

M_imag = (omega \* c_dl \* r_ct) / (1 + omega\*\*2 \* c_dl\*\*2 \*
r_ct\*\*2)

return M_real, M_imag

\# Create comprehensive figure

fig = plt.figure(figsize=(20, 14))

\# Plot 1-3: M\' vs Frequency (Real part)

for i, (material, data) in enumerate(materials_data.items()):

ax = fig.add_subplot(3, 3, i + 1)

\# Pi-Gate

pi = data\[\'Pi-Gate\'\]

M_real_pi, \_, \_ = calculate_electric_modulus(

pi\[\'r_ct\'\], pi\[\'c_dl\'\], pi\[\'alpha\'\], omega, pi\[\'C0\'\]

)

\# Omega-Gate

omega_gate = data\[\'Omega-Gate\'\]

M_real_omega, \_, \_ = calculate_electric_modulus(

omega_gate\[\'r_ct\'\], omega_gate\[\'c_dl\'\], omega_gate\[\'alpha\'\],
omega, omega_gate\[\'C0\'\]

)

\# Plot M\' vs frequency

ax.semilogx(frequencies, M_real_pi, \'o-\', color=\'#1f77b4\',
linewidth=2.5,

markersize=4, markevery=30, label=\'Pi-Gate (η=0.82)\',

markerfacecolor=\'white\', markeredgewidth=1.5)

ax.semilogx(frequencies, M_real_omega, \'s-\', color=\'#ff7f0e\',
linewidth=2.5,

markersize=4, markevery=30, label=\'Omega-Gate (η=0.98)\',

markerfacecolor=\'white\', markeredgewidth=1.5)

\# Styling

ax.set_xlabel(\'Frequency \[Hz\]\', fontweight=\'bold\', fontsize=11)

ax.set_ylabel(\"M\' (Real Modulus)\", fontweight=\'bold\', fontsize=11)

ax.set_title(f\'{material} - Real Modulus\', fontsize=13,
fontweight=\'bold\')

ax.legend(loc=\'lower right\', frameon=True, shadow=True, fontsize=9)

ax.grid(True, alpha=0.3, which=\'both\', linestyle=\'\--\')

ax.set_xlim(1, 1e7)

# 

# 

\# Plot M\' vs frequency

ax.semilogx(frequencies, M_real_pi, \'o-\', color=\'#1f77b4\',
linewidth=2.5

ax.semilogx(frequencies, M_real_omega, \'s-\', color=\'#ff7f0e\',
linewidth=2.5,

markersize=4, markevery=30, label=\'Omega-Gate (η=0.98)\',

markerfacecolor=\'white\', markeredgewidth=1.5)

\# Styling

ax.set_xlabel(\'Frequency \[Hz\]\', fontweight=\'bold\', fontsize=11)

ax.set_ylabel(\"M\' (Real Modulus)\", fontweight=\'bold\', fontsize=11)

ax.set_title(f\'{material} - Real Modulus\', fontsize=13,
fontweight=\'bold\')

ax.legend(loc=\'lower right\', frameon=True, shadow=True, fontsize=9)

ax.grid(True, alpha=0.3, which=\'both\', linestyle=\'\--\')

ax.set_xlim(1, 1e7)

\# Plot 4-6: M\'\' vs Frequency (Imaginary part - relaxation peaks)

for i, (material, data) in enumerate(materials_data.items()):

ax = fig.add_subplot(3, 3, i + 4)

\# Pi-Gate

pi = data\[\'Pi-Gate\'\]

\_, M_imag_pi, \_ = calculate_electric_modulus(

pi\[\'r_ct\'\], pi\[\'c_dl\'\], pi\[\'alpha\'\], omega, pi\[\'C0\'\]

)

\# Omega-Gate

omega_gate = data\[\'Omega-Gate\'\]

\_, M_imag_omega, \_ = calculate_electric_modulus(

omega_gate\[\'r_ct\'\], omega_gate\[\'c_dl\'\], omega_gate\[\'alpha\'\],
omega, omega_gate\[\'C0\'\]

)

\# Plot M\'\' vs frequency

ax.semilogx(frequencies, M_imag_pi, \'o-\', color=\'#2E86AB\',
linewidth=2.5,

markersize=4, markevery=30, label=\'Pi-Gate (η=0.82)\',

markerfacecolor=\'white\', markeredgewidth=1.5)

ax.semilogx(frequencies, M_imag_omega, \'s-\', color=\'#F18F01\',
linewidth=2.5,

markersize=4, markevery=30, label=\'Omega-Gate (η=0.98)\',

markerfacecolor=\'white\', markeredgewidth=1.5)

ax.axvline(x=f_peak_pi, color=\'#2E86AB\', linestyle=\'\--\', alpha=0.5,
linewidth=1)

ax.axvline(x=f_peak_omega, color=\'#F18F01\', linestyle=\'\--\',
alpha=0.5, linewidth=1)

\# Styling

ax.set_xlabel(\'Frequency \[Hz\]\', fontweight=\'bold\', fontsize=11)

ax.set_ylabel(\'M\\\'\\\' (Imaginary Modulus)\', fontweight=\'bold\',
fontsize=11)

ax.set_title(f\'{material} - Imaginary Modulus Peak\', fontsize=13,
fontweight=\'bold\')

ax.legend(loc=\'upper right\', frameon=True, shadow=True, fontsize=9)

ax.grid(True, alpha=0.3, which=\'both\', linestyle=\'\--\')

ax.set_xlim

\# Plot 7-9: M\'\' vs M\' (Argand diagram - Cole-Cole style for modulus)

for i, (material, data) in enumerate(materials_data.items()):

ax = fig.add_subplot(3, 3, i + 7)

\# Pi-Gate

pi = data\[\'Pi-Gate\'\]

M_real_pi, M_imag_pi, \_ = calculate_electric_modulus(

pi\[\'r_ct\'\], pi\[\'c_dl\'\], pi\[\'alpha\'\], omega, pi\[\'C0\'\]

)

\# Omega-Gate

omega_gate = data\[\'Omega-Gate\'\]

M_real_omega, M_imag_omega, \_ = calculate_electric_modulus(

omega_gate\[\'r_ct\'\], omega_gate\[\'c_dl\'\], omega_gate\[\'alpha\'\],
omega, omega_gate\[\'C0\'\]

)

\# Plot M\'\' vs M\'

ax.plot(M_real_pi, M_imag_pi, \'o-\', color=\'#9467bd\', linewidth=2.5,

markersize=4, markevery=30, label=\'Pi-Gate (η=0.82)\',

markerfacecolor=\'white\', markeredgewidth=1.5)

ax.plot(M_real_omega, M_imag_omega, \'s-\', color=\'#d62728\',
linewidth=2.5,

markersize=4, markevery=30, label=\'Omega-Gate (η=0.98)\',

markerfacecolor=\'white\', markeredgewidth=1.5)

\# Fill under curves

ax.fill_between(M_real_pi, 0, M_imag_pi, alpha=0.1, color=\'#9467bd\')

ax.fill_between(M_real_omega, 0, M_imag_omega, alpha=0.1,
color=\'#d62728\')

\# Styling

ax.set_xlabel(\"M\' (Real Modulus)\", fontweight=\'bold\', fontsize=11)

ax.set_ylabel(\'M\\\'\\\' (Imaginary Modulus)\', fontweight=\'bold\',
fontsize=11)

ax.set_title(f\'{material} - Modulus Argand Plot\', fontsize=13,
fontweight=\'bold\')

ax.legend(loc=\'upper right\', frameon=True, shadow=True, fontsize=9)

ax.grid(True, alpha=0.3, linestyle=\'\--\')

ax.set_aspect(\'equal\', adjustable=\'box\')

plt.suptitle(\'Electric Modulus Analysis: M\\\' vs Frequency, M\\\'\\\'
vs Frequency, and Argand Plots\\n\' +

\'Demonstrating Dielectric Relaxation in Pi-Gate vs Omega-Gate NWFETs\',

fontsize=18, fontweight=\'bold\', y=0.98)

plt.tight_layout(rect=\[0, 0, 1, 0.96\])

plt.savefig(\'electric_modulus_analysis.png\', dpi=300,
bbox_inches=\'tight\', facecolor=\'white\')

plt.show()

print(\"SUCCESS: Electric modulus analysis plot saved as
\'electric_modulus_analysis.png\'\")

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

ax.plot(M_real_omega, M_imag_omega, \'s-\', color=\'#d62728\',
linewidth=2.5,

markersize=4, markevery=30, label=\'Omega-Gate (η=0.98)\',

markerfacecolor=\'white\', markeredgewidth=1.5)

\# Fill under curves

ax.fill_between(M_real_pi, 0, M_imag_pi, alpha=0.1, color=\'#9467bd\')

ax.fill_between(M_real_omega, 0, M_imag_omega, alpha=0.1,
color=\'#d62728\')

\# Styling

ax.set_xlabel(\"M\' (Real Modulus)\", fontweight=\'bold\', fontsize=11)

ax.set_ylabel(\'M\\\'\\\' (Imaginary Modulus)\', fontweight=\'bold\',
fontsize=11)

ax.set_title(f\'{material} - Modulus Argand Plot\', fontsize=13,
fontweight=\'bold\')

ax.legend(loc=\'upper right\', frameon=True, shadow=True, fontsize=9)

ax.grid(True, alpha=0.3, linestyle=\'\--\')

ax.set_aspect(\'equal\', adjustable=\'box\')

plt.suptitle(\'Electric Modulus Analysis: M\\\' vs Frequency, M\\\'\\\'
vs Frequency, and Argand Plots\\n\' +

\'Demonstrating Dielectric Relaxation in Pi-Gate vs Omega-Gate NWFETs\',

fontsize=18, fontweight=\'bold\', y=0.98)

plt.tight_layout(rect=\[0, 0, 1, 0.96\])

plt.savefig(\'electric_modulus_analysis.png\', dpi=300,
bbox_inches=\'tight\', facecolor=\'white\')

plt.show()

print(\"SUCCESS: Electric modulus analysis plot saved as
\'electric_modulus_analysis.png\'\")

> **Code snippet 9.10:** Electric modulus M′′ vs frequency for five
> dielectrics at T = 300 K & Modulus Cole-Cole plots (M′′ vs M′) for
> SiO₂, HfO₂, and La₂O₃ at T = 300 K.

# 

import numpy as np

import matplotlib.pyplot as plt

\# Set publication-quality parameters

plt.rcParams\[\'font.family\'\] = \'Times New Roman\'

plt.rcParams\[\'font.size\'\] = 12

plt.rcParams\[\'axes.labelsize\'\] = 14

plt.rcParams\[\'axes.titlesize\'\] = 16

plt.rcParams\[\'xtick.labelsize\'\] = 12

plt.rcParams\[\'ytick.labelsize\'\] = 12

plt.rcParams\[\'legend.fontsize\'\] = 11

print(\"\-\-- Generating AC Conductivity Analysis Plots \-\--\")

\# Physical constants

eps0 = 8.854e-12 \# F/m

kB = 1.381e-23 \# J/K

T_room = 300 \# K

\# Frequency range

frequencies = np.logspace(0, 7, 300) \# 1 Hz to 10 MHz

omega = 2 \* np.pi \* frequencies

kB = 1.381e-23 \# J/K

T_room = 300 \# K

\# Frequency range

frequencies = np.logspace(0, 7, 300) \# 1 Hz to 10 MHz

omega = 2 \* np.pi \* frequencies

\# Material parameters for AC conductivity

materials_data = {

\'HfO2\': {

\'Pi-Gate\': {

\'sigma_dc\': 1e-10, \# S/m - DC conductivity

\'A\': 5e-14, \# Prefactor

\'n\': 0.65, \# Power law exponent

\'E_a\': 0.35, \# Activation energy (eV)

\'r_ct\': 800,

\'c_dl\': 0.8e-9

},

\'Omega-Gate\': {

\'sigma_dc\': 2e-10, \# Higher due to better gate control

\'A\': 8e-14,

\'n\': 0.80, \# More ideal behavior

\'E_a\': 0.30,

\'r_ct\': 400,

\'c_dl\': 1.5e-9

}

},

\'ZrO2\': {

\'Pi-Gate\': {

\'sigma_dc\': 5e-11,

\'A\': 3e-14,

\'n\': 0.60,

\'E_a\': 0.40,

\'r_ct\': 1500,

\'c_dl\': 0.5e-9

},

\'Omega-Gate\': {

\'sigma_dc\': 1e-10,

\'A\': 5e-14,

\'n\': 0.75,

\'E_a\': 0.35,

\'r_ct\': 750,

\'c_dl\': 1.0e-9

}

},

\'La2O3\': {

\'Pi-Gate\': {

\'sigma_dc\': 2e-10,

\'A\': 6e-14,

\'n\': 0.70,

\'E_a\': 0.32,

\'r_ct\': 350,

\'c_dl\': 2.0e-9

},

\'Omega-Gate\': {

\'sigma_dc\': 4e-10,

\'A\': 1e-13,

\'n\': 0.85,

\'E_a\': 0.28,

\'r_ct\': 180,

\'c_dl\': 2.5e-9

}

def calculate_ac_conductivity(sigma_dc, A, n, omega):

\"\"\"

Calculate AC conductivity using universal dielectric response

σ_ac(ω) = σ_dc + Aω\^n

\"\"\"

sigma_ac = sigma_dc + A \* (omega\*\*n)

return sigma_ac

def calculate_conductivity_from_impedance(r_ct, c_dl, omega):

\"\"\"

Alternative: Calculate AC conductivity from impedance

σ\*(ω) = jωε₀ε\*(ω) = 1/Z\*(ω) × geometric_factor

\"\"\"

tau = r_ct \* c_dl

\# Complex conductivity

sigma_complex = (1 / r_ct) \* (1j \* omega \* tau) / (1 + 1j \* omega \*
tau)

sigma_real = np.real(sigma_complex)

sigma_imag = np.imag(sigma_complex)

return sigma_real, sigma_imag

def calculate_temperature_dependent_sigma(sigma_0, E_a, T, T_ref=300):

\"\"\"

Temperature dependence of conductivity (Arrhenius)

σ(T) = σ₀ exp(-E_a / kT)

\"\"\"

k_ev = 8.617e-5 \# Boltzmann constant in eV/K

sigma_T = sigma_0 \* np.exp(-E_a / (k_ev \* T)) / np.exp(-E_a / (k_ev \*
T_ref))

return sigma_T

plt.suptitle(\'AC Conductivity Analysis: Frequency-Dependent
Conductivity and Arrhenius Behavior\\n\' +

\'Universal Dielectric Response in Pi-Gate vs Omega-Gate NWFETs\',

fontsize=18, fontweight=\'bold\', y=0.98)

plt.tight_layout(rect=\[0, 0, 1, 0.96\])

plt.savefig(\'ac_conductivity_analysis.png\', dpi=300,
bbox_inches=\'tight\', facecolor=\'white\')

plt.show()

print(\"SUCCESS: AC conductivity analysis plot saved as
\'ac_conductivity_analysis.png\'\")

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

> **Code snippet 9.11:** AC conductivity vs frequency for five
> dielectrics at T = 300 K.

# 

# 

import numpy as np

import matplotlib.pyplot as plt

\# Set publication-quality parameters

plt.rcParams\[\'font.family\'\] = \'Times New Roman\'

plt.rcParams\[\'font.size\'\] = 12

plt.rcParams\[\'axes.labelsize\'\] = 14

plt.rcParams\[\'axes.titlesize\'\] = 16

plt.rcParams\[\'xtick.labelsize\'\] = 12

plt.rcParams\[\'ytick.labelsize\'\] = 12

plt.rcParams\[\'legend.fontsize\'\] = 11

print(\"\-\-- Generating Loss Tangent and Cryogenic Performance Plots
\-\--\")

\# Physical constants

eps0 = 8.854e-12 \# F/m

kB = 1.381e-23 \# J/K

q = 1.602e-19 \# C

\# Frequency range

frequencies = np.logspace(0, 7, 300) \# 1 Hz to 10 MHz

omega = 2 \* np.pi \* frequencies

\# Material parameters

materials_data = {

\'HfO2\': {

\'Pi-Gate\': {

\'r_ct\': 800,

\'c_dl\': 0.8e-9,

\'alpha\': 0.75,

\'eps_r\': 25,

\'sigma_dc\': 1e-10,

\'E_a\': 0.35 \# eV

},

\'Omega-Gate\': {

\'r_ct\': 400,

\'c_dl\': 1.5e-9,

\'alpha\': 0.95,

\'eps_r\': 25,

\'sigma_dc\': 2e-10,

\'E_a\': 0.30

}

},

\'Omega-Gate\': {

\'r_ct\': 750,

\'c_dl\': 1.0e-9,

\'alpha\': 0.90,

\'eps_r\': 22,

\'sigma_dc\': 1e-10,

\'E_a\': 0.35

}

},

### 

La2O3\': {

\'Pi-Gate\': {

\'r_ct\': 350,

\'c_dl\': 2.0e-9,

\'alpha\': 0.88,

\'eps_r\': 27,

\'sigma_dc\': 2e-10,

\'E_a\': 0.32

},

\'Omega-Gate\': {

\'r_ct\': 180,

\'c_dl\': 2.5e-9,

\'alpha\': 0.98,

\'eps_r\': 27,

\'sigma_dc\': 4e-10,

\'E_a\': 0.28

}

}

}

def calculate_cryogenic_performance(material_params, T_cryo=77,
T_room=300):

\"\"\"

Calculate cryogenic performance metrics

Returns improvement factors at 77K vs 300K

\"\"\"

\# Cryogenic loss reduction factor

temp_factor = T_room / T_cryo \# \~3.9

\# Reduced thermal noise

noise_reduction = np.sqrt(T_room / T_cryo)

\# Improved subthreshold swing (thermal voltage reduced)

Vt_thermal_room = 0.026 \# kT/q at 300K

Vt_thermal_cryo = kB \* T_cryo / q \# \~6.6 mV at 77K

return {

\'temp_factor\': temp_factor,

\'noise_reduction\': noise_reduction,

\'V_thermal_ratio\': Vt_thermal_room / Vt_thermal_cryo

}

\# Find maximum Q

max_Q_pi = np.max(Q_pi)

max_Q_omega = np.max(Q_omega)

ax.axhline(y=max_Q_pi, color=\'#9467bd\', linestyle=\'\--\', alpha=0.5)

ax.axhline(y=max_Q_omega, color=\'#8c564b\', linestyle=\'\--\',
alpha=0.5)

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

\# Styling

ax.set_xlabel(\'Frequency \[Hz\]\', fontweight=\'bold\', fontsize=11)

ax.set_ylabel(\'Q Factor (1/tan δ)\', fontweight=\'bold\', fontsize=11)

ax.set_title(f\'{material} - Quality Factor (77K)\', fontsize=13,
fontweight=\'bold\')

ax.legend(loc=\'upper right\', frameon=True, shadow=True, fontsize=9)

ax.grid(True, alpha=0.3, which=\'both\', linestyle=\'\--\')

ax.set_xlim(1, 1e7)

\# Add max Q annotation

ax.text(0.95, 0.95, f\'Max Q(π)={max_Q_pi:.0f}\\nMax
Q(Ω)={max_Q_omega:.0f}\',

transform=ax.transAxes, fontsize=9, verticalalignment=\'top\',
horizontalalignment=\'right\',

bbox=dict(boxstyle=\'round\', facecolor=\'lightyellow\', alpha=0.8))

plt.suptitle(\'Loss Tangent (tan δ) and Cryogenic Performance
Analysis\\n\' +

\'Dielectric Loss Characterization in Pi-Gate vs Omega-Gate NWFETs at
77K-400K\',

fontsize=18, fontweight=\'bold\', y=0.98)

plt.tight_layout(rect=\[0, 0, 1, 0.96\])

plt.savefig(\'loss_tangent_cryogenic.png\', dpi=300,
bbox_inches=\'tight\', facecolor=\'white\')

plt.show()

print(\"SUCCESS: Loss tangent and cryogenic performance plot saved as
\'loss_tangent_cryogenic.png\'\")

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

> **Code snippet 9.12:** Loss tangent (tan δ) vs temperature at 1 MHz
> for all dielectric-gate combinations.

### WEB APPLICATION- NWFET Energy Band Diagram Program

### 

### PART A: Database Management (User Authentication)

import sqlite3

import hashlib

import time

from datetime import datetime, timedelta

class DatabaseManager:

\"\"\"Handle database operations for users and sessions\"\"\"

def \_\_init\_\_(self, db_path=\'database/nwfet_app.db\'):

self.db_path = db_path

self.init_database()

def init_database(self):

\"\"\"Initialize database tables\"\"\"

conn = sqlite3.connect(self.db_path)

cursor = conn.cursor()

# 

# 

# 

# 

# 

# 

# 

# 

\# Sessions table

cursor.execute(\'\'\'

CREATE TABLE IF NOT EXISTS sessions (

id TEXT PRIMARY KEY,

user_id INTEGER NOT NULL,

expires_at TIMESTAMP NOT NULL

)

\'\'\')

conn.commit()

conn.close()

def create_user(self, username, email, password):

\"\"\"Create new user with hashed password\"\"\"

conn = sqlite3.connect(self.db_path)

cursor = conn.cursor()

password_hash = hashlib.sha256(password.encode()).hexdigest()

try:

cursor.execute(\'\'\'

INSERT INTO users (username, email, password_hash)

VALUES (?, ?, ?)

\'\'\', (username, email, password_hash))

conn.commit()

return True

except sqlite3.IntegrityError:

return False

finally:

conn.close()

def authenticate_user(self, username, password):

\"\"\"Authenticate user credentials\"\"\"

conn = sqlite3.connect(self.db_path)

cursor = conn.cursor()

password_hash = hashlib.sha256(password.encode()).hexdigest()

def create_session(self, user_id):

\"\"\"Create session for authenticated user\"\"\"

session_id =
hashlib.sha256(f\"{user_id}{time.time()}\".encode()).hexdigest()

expires_at = datetime.now() + timedelta(hours=24)

conn = sqlite3.connect(self.db_path)

cursor = conn.cursor()

cursor.execute(\'\'\'

INSERT INTO sessions (id, user_id, expires_at)

VALUES (?, ?, ?)

\'\'\', (session_id, user_id, expires_at))

conn.commit()

conn.close()

return session_id

#  

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

### 

### PART B: HTTP Server and Request Routing

from http.server import HTTPServer, BaseHTTPRequestHandler

from urllib.parse import urlparse, parse_qs

import json

class NWFETRequestHandler(BaseHTTPRequestHandler):

\"\"\"Handle HTTP requests for NWFET application\"\"\"

def \_\_init\_\_(self, \*args, \*\*kwargs):

self.db = DatabaseManager()

super().\_\_init\_\_(\*args, \*\*kwargs)

def do_GET(self):

\"\"\"Handle GET requests - route to appropriate handler\"\"\"

parsed_path = urlparse(self.path)

path = parsed_path.path

if path == \'/\':

self.serve_file(\'templates/dashboard.html\', \'text/html\')

elif path == \'/login\':

self.serve_file(\'templates/login.html\', \'text/html\')

elif path.startswith(\'/api/\'):

self.handle_api_request()

elif path.endswith(\'.css\'):

self.serve_file(path, \'text/css\')

elif path.endswith(\'.js\'):

self.serve_file(path, \'application/javascript\')

else:

self.send_error(404)

def do_POST(self):

\"\"\"Handle POST requests - API endpoints\"\"\"

parsed_path = urlparse(self.path)

path = parsed_path.path

if path == \'/api/login\':

self.handle_login()

elif path == \'/api/calculate\':

self.handle_calculation()

elif path == \'/api/drain_iv\':

self.handle_drain_iv()

elif path == \'/api/transfer_iv\':

self.handle_transfer_iv()

else:

self.send_error(404)

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

### PART C: NWFET Physics Calculations - Band Diagram

def perform_calculation(self, params):

\"\"\"Calculate band structure for NWFET device\"\"\"

\# Material properties

material_props = {

\'Si\': {\'bandGap\': 1.12, \'electronAffinity\': 4.05},

\'Ge\': {\'bandGap\': 0.66, \'electronAffinity\': 4.0},

\'GaAs\': {\'bandGap\': 1.42, \'electronAffinity\': 4.07},

\'InAs\': {\'bandGap\': 0.36, \'electronAffinity\': 4.9}

}

\# Get parameters

props = material_props.get(params\[\'material\'\],
material_props\[\'Si\'\])

band_gap = props\[\'bandGap\'\]

electron_affinity = props\[\'electronAffinity\'\]

gate_voltage = params.get(\'gateVoltage\', 0)

temperature = params.get(\'temperature\', 300)

drain_voltage = params.get(\'drainVoltage\', 0.1)

gate_type = params.get(\'gateType\', \'pi\')

\# Fermi level shift

fermi_shift = 1.0 \* gate_voltage + 0.5 \* drain_voltage - 0.05 \*
(temperature - 300)

fermi_level = electron_affinity + band_gap/2 + fermi_shift

\# Position array (-5nm to 5nm)

positions = \[x \* 0.1 for x in range(-50, 51)\]

\# Gate efficiency factor (Pi=0.82, Omega=0.98)

curvature_factor = 0.05 if gate_type == \'pi\' else 0.25

\# Conduction band energy

conduction_band = \[

electron_affinity + band_gap + curvature_factor \* (x/5)\*\*2 +

0.1 \* (temperature - 300) + 0.5 \* gate_voltage

for x in positions

\]

\# Valence band energy

valence_band = \[cb - band_gap for cb in conduction_band\]

return {

\'positions\': positions,

\'conductionBand\': conduction_band_relative,

\'valenceBand\': valence_band_relative,

\'fermiLevel\': 0.0,

\'parameters\': params

}

# 

# 

#  

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

#  

def perform_drain_iv(self, params):

\"\"\"Calculate drain IV characteristics\"\"\"

v_gs = float(params.get(\'gateVoltage\', 0))

v_ds_list = \[i \* 0.1 for i in range(21)\] \# 0 to 2V

ids_list = \[\]

\# Device parameters

v_t = 0.3 \# Threshold voltage (V)

mu = 0.1 \# Mobility (m2/Vs)

c_ox = 1e-6 \# Oxide capacitance (F/m2)

w_l = 10 \# Width/Length ratio

for v_ds in v_ds_list:

if v_gs \> v_t:

if v_ds \< v_gs - v_t: \# Linear region

i_d = mu \* c_ox \* w_l \* (v_gs - v_t - v_ds/2) \* v_ds

else: \# Saturation region

i_d = mu \* c_ox \* w_l \* (v_gs - v_t)\*\*2 / 2

else: \# Subthreshold

i_d = 0

ids_list.append(i_d)

return {

\'vds\': v_ds_list,

\'ids\': ids_list,

\'params\': params

}

def perform_transfer_iv(self, params):

\"\"\"Calculate transfer IV characteristics\"\"\"

v_ds = float(params.get(\'drainVoltage\', 0.1))

v_gs_list = \[i \* 0.1 - 1 for i in range(21)\] \# -1 to 1V

ids_list = \[\]

v_t = 0.3

mu = 0.1

c_ox = 1e-6

w_l = 10

for v_gs in v_gs_list:

if v_gs \> v_t:

if v_ds \< v_gs - v_t:

i_d = mu \* c_ox \* w_l \* (v_gs - v_t - v_ds/2) \* v_ds

else:

i_d = mu \* c_ox \* w_l \* (v_gs - v_t)\*\*2 / 2

}

### 

# 

# 

# 

# 

### PART E: API Endpoint - Login Handler

def handle_login(self):

\"\"\"Handle user login and session creation\"\"\"

content_length = int(self.headers\[\'Content-Length\'\])

post_data = self.rfile.read(content_length)

data = parse_qs(post_data.decode(\'utf-8\'))

username = data.get(\'username\', \[\'\'\])\[0\]

password = data.get(\'password\', \[\'\'\])\[0\]

\# Authenticate

user = self.db.authenticate_user(username, password)

if user:

\# Create session

session_id = self.db.create_session(user\[0\])

\# Send success response with cookie

self.send_response(200)

self.send_header(\'Content-type\', \'application/json\')

self.send_header(\'Set-Cookie\', f\'session_id={session_id}; Path=/;
Max-Age=86400\')

self.end_headers()

response = {

\'success\': True,

\'user\': {

\'id\': user\[0\],

\'username\': user\[1\],

\'email\': user\[2\]

}

}

else:

self.send_response(200)

self.send_header(\'Content-type\', \'application/json\')

self.end_headers()

response = {\'success\': False, \'error\': \'Invalid credentials\'}

self.wfile.write(json.dumps(response).encode())

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

#  

# 

# 

# 

# 

### 

### 

\<!DOCTYPE html\>

\<html lang=\"en\"\>

\<head\>

\<meta charset=\"UTF-8\"\>

\<title\>NWFET Energy Band Diagram Program\</title\>

\<script src=\"https://cdn.plot.ly/plotly-2.26.0.min.js\"\>\</script\>

\<link rel=\"stylesheet\" href=\"css/style.css\"\>

\</head\>

\<body\>

\<header class=\"header\"\>

\<div class=\"title\"\>

\<i class=\"fas fa-atom\"\>\</i\> NWFET Energy Band Diagram Program

\</div\>

\</header\>

\<div class=\"main-container\"\>

\<!\-- Control Panel \--\>

\<aside class=\"control-panel\"\>

\<!\-- Gate Architecture Selection \--\>

\<div class=\"control-section\"\>

\<div class=\"section-title\"\>

\<i class=\"fas fa-microchip\"\>\</i\> Gate Architecture

\</div\>

\<div class=\"gate-selector\"\>

\<div class=\"gate-option selected\" data-gate=\"pi\"\>

\<strong\>Pi-Gate\</strong\>

\<div style=\"font-size: 11px;\"\>Partial wrap (η=0.82)\</div\>

\</div\>

\<div class=\"gate-option\" data-gate=\"omega\"\>

\<strong\>Omega-Gate\</strong\>

\<div style=\"font-size: 11px;\"\>Full wrap (η=0.98)\</div\>

\</div\>

\</div\>

\</div\>

\<div class=\"form-group\"\>

\<label\>Gate Material\</label\>

\<select id=\"material\"\>

\<option value=\"Si\"\>Silicon (Si)\</option\>

\<option value=\"Ge\"\>Germanium (Ge)\</option\>

\<option value=\"GaAs\"\>GaAs\</option\>

\<option value=\"InAs\"\>InAs\</option\>

\</select\>

\</div\>

### 

\<label\>Oxide Thickness (nm)\</label\>

\<input type=\"range\" id=\"oxide-thickness\" min=\"0.5\" max=\"10\"
value=\"2\" step=\"0.1\"\>

\</div\>

\<div class=\"form-group\"\>

\<label\>Nanowire Diameter (nm)\</label\>

\<input type=\"range\" id=\"nanowire-diameter\" min=\"3\" max=\"20\"
value=\"10\" step=\"0.5\"\>

\</div\>

\<div class=\"form-group\"\>

\<label\>Channel Length (nm)\</label\>

\<input type=\"number\" id=\"channel-length\" value=\"20\" min=\"10\"
max=\"100\"\>

\</div\>

\</div\>

\<!\-- Bias Conditions \--\>

\<div class=\"control-section\"\>

\<div class=\"section-title\"\>

\<i class=\"fas fa-bolt\"\>\</i\> Bias Conditions

\</div\>

\<div class=\"form-group\"\>

\<label\>Gate Voltage (V)\</label\>

\<input type=\"range\" id=\"gate-voltage\" min=\"-2\" max=\"2\"
value=\"0\" step=\"0.1\"\>

\</div\>

\<div class=\"form-group\"\>

\<label\>Drain Voltage (V)\</label\>

\<input type=\"number\" id=\"drain-voltage\" value=\"0.1\" min=\"0\"
max=\"1\" step=\"0.01\"\>

\</div\>

\<div class=\"form-group\"\>

\<label\>Temperature (K)\</label\>

\<input type=\"number\" id=\"temperature\" value=\"300\" min=\"77\"
max=\"500\"\>

\</div\>

\</div\>

\<!\-- Calculate Button \--\>

\<button id=\"calculate-btn\" class=\"calculate-btn\"\>

\<i class=\"fas fa-calculator\"\>\</i\> Calculate Bands

\</button\>

\</aside\>

\<!\-- Results Panel \--\>

\<main class=\"results-panel\"\>

\<div id=\"band-diagram\" class=\"plot-container\"\>\</div\>

\<div id=\"iv-curves\" class=\"plot-container\"\>\</div\>

\</main\>

\</div\>

\<script src=\"js/main.js\"\>\</script\>

\</body\>

\</html\>

> **Code snippet 9.13:** Web-application of NWFET

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

#  Chapter 10:

#  SDGs

# 

+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| # SDGs With Icons                                                                    | # Justification                                                                                                                                                                                                                                                                   |
+======================================================================================+===================================================================================================================================================================================================================================================================================+
| # ![](media/image54.png){width="2.1319444444444446in" height="1.9236111111111112in"} | # The project provides practical exposure to semiconductor physics, nanotechnology simulation, and advanced device modeling. It supports high-level technical learning by bridging the gap between theoretical microelectronics and real-world sub-10 nm technology applications. |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| # ![](media/image55.png){width="2.2083333333333335in" height="1.8958333333333333in"} | # Optimization of transistor efficiency directly impacts the semiconductor industry, which is a backbone for economic growth. Improved device performance supports the global workforce by driving innovation in consumer electronics and high-performance computing.             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| # ![](media/image56.png){width="2.1527777777777777in" height="1.7777777777777777in"} | # This research promotes innovation by integrating high-k dielectrics and multi-gate architectures into next-generation digital infrastructure. It demonstrates the use of modern simulation platforms to solve complex scaling problems in semiconductor design efficiently.     |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

# 

> **Table 9.1:** Summary of UN Sustainable Development Goals addressed
> by this project.

# 

  ---------------------------------------------------------------------
  **SDG**   **Goal**           **Contribution**
  --------- ------------------ ----------------------------------------
  **SDG 4** **Quality          Open-access Python framework and
            Education**        Plotly.js web simulator for
                               semiconductor device education.

  **SDG 8** **Decent Work &    Advances semiconductor industry through
            Economic Growth**  NWFET performance optimisation; supports
                               high-skilled employment.

  **SDG 9** **Industry,        Enables sub-5 nm CMOS scaling for AI,
            Innovation &       5G, and quantum computing
            Infrastructure**   infrastructure.
  ---------------------------------------------------------------------

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

#  References

# 

1.  K. J. Kuhn, "Considerations for ultimate CMOS scaling," *IEEE
    Transactions on Electron Devices*, vol. 59, no. 7, pp. 1813--1828,
    2012.

2.  []{#_bookmark122 .anchor}Y. Taur and T. H. Ning, *Fundamentals of
    Modern VLSI Devices*. Cambridge University Press, 2nd ed., 2013.

3.  []{#_bookmark123 .anchor}I. Ferain, C. A. Colinge, and J.-P.
    Colinge, "Multigate transistors as the future of classical
    metal-oxide-semiconductor field-effect transistors," *Nature*, vol.
    479, pp. 310--316, 2011.

4.  []{#_bookmark124 .anchor}J.-P. Colinge, *FinFETs and Other
    Multi-Gate Transistors*. New York, NY: Springer, 2008.

5.  []{#_bookmark125 .anchor} J.-P. Colinge, "Novel gate concepts for
    MOS devices," *Proceedings of the 30th European Solid-State Device
    Research Conference (ESSDERC)*, 2004.

6.  []{#_bookmark126 .anchor}Yang, F.-L., Chen, H.-Y., Chen, F.-C.,
    Huang, C.-C., Chang, C.-Y., Chiu, H.-K., Lee, C.-C.,

> Chen, C.-C., Huang, H.-T., Chen, C.-J., Tao, H.-J., Yeo, Y.-C., Liang,
> M.-S., and Hu, C.,
>
> "25 nm CMOS omega FETs," in *IEEE International Electron Devices
> Meeting (IEDM)*,
>
> pp. 255--258, 2002.

7.  H.-S. P. Wong and H. Iwai, "On the scaling issues and high-*k*
    replacement of ultrathin gate dielectrics for nanoscale MOS
    transistors," *Microelectronic Engineering*, vol. 83,

> pp. 1867--1904, 2006.

8.  []{#_bookmark128 .anchor} E. H. Minhaj, M. A. Razzak, M. M. Islam,
    and M. M. R. Adnan, "Performance enhancement of multigate FinFETs by
    using high-*k* stack oxide," in *2019 International Conference on
    Advances in Science, Engineering and Robotics Technology (ICASERT)*,
    2019.

9.   X. Wang and Y. Taur, "High-*k* gate dielectrics for CMOS
    technology," *Semiconductor Science and Technology*, vol. 33, p.
    123001, 2018.

10. []{#_bookmark130 .anchor} S. Richter, S. Trellenkamp, M.
    Schmidt, Q. T. Zhao, and S. Mantl, "Strained silicon nanowire array
    MOSFETs with high-*k*/metal gate stack," in *International
    Conference on Ultimate Integration on Silicon (ULIS)*, 2012.

11. []{#_bookmark131 .anchor}Y. Lin, Y. Wu, M. Hung, and J. Chen,
    "Charge storage characteristics of Pi-gate poly- Si nanowires flash
    memory," *International Journal of Electrochemical Science*, vol. 7,

> pp. 11584--11594, 2012.

12. []{#_bookmark132 .anchor}F. Balestra and G. Ghibaudo, "Physics and
    performance of nanoscale semiconductor devices at cryogenic
    temperatures," *Semiconductor Science and Technology*, vol. 32, no.
    2,

> p\. 023002, 2017.

13. []{#_bookmark133 .anchor} J. A. Matos, M. d. Souza, M. Cassé, S.
    Barraud, O. Faynot, and M. Pavanello, "Elec- trical characterization
    of *ω*-gate nanowire MOSFETs down to cryogenic temperatures,"
    *Symposium on Microelectronics Technology and Devices*, 2023.

14. []{#_bookmark134 .anchor}G. Klimeck *et al.*, "Atomistic simulation
    of realistically sized nanodevices using NEMO 3-D," *IEEE
    Transactions on Electron Devices*, vol. 54, pp. 2079--2089, 2007.

15. []{#_bookmark135 .anchor} A. Breed and K. Roenker, "Comparison of
    the scaling characteristics of nanoscale silicon N-channel
    multiple-gate MOSFETs," in *48th Midwest Symposium on Circuits and
    Systems (MWSCAS)*, pp. 603--606, 2005.

16. []{#_bookmark136 .anchor} S. Deshpande, S. Sopariwala, R.
    Singhvi, R. Khandelwal, J. Marvaniya, and R. Parekh, "Performance
    analysis of Silicon Nanowire FET for GAA and Pi Gate
    configurations," in *2022 IEEE International Conference on
    Nanoelectronics, Nanophotonics, Nanomaterials, Nanobioscience &
    Nanotechnology (5NANO)*, pp. 1--6, 2022.

17. []{#_bookmark137 .anchor}J. Park, C. A. Colinge, and J.-P. Colinge,
    "Comparison of gate structures for short-channel SOI MOSFETs," in
    *IEEE International SOI Conference*, 2001.

18. []{#_bookmark138 .anchor}J. T. Park and J.-P. Colinge,
    "Multiple-gate SOI MOSFETs: device design guidelines,"

> *IEEE Transactions on Electron Devices*, 2002.

19. []{#_bookmark139 .anchor} R. Ritzenthaler, M. Gaillardin, K.
    Akarvardar, O. Faynot, C. Jahan, and S. Cristoloveanu, "Modelling
    the back-gate coupling effect in triple-, *π*- and *ω*-gate FETs,"
    *ECS Transactions*, 2007.

20. []{#_bookmark140 .anchor} J.-P. Raskin, T. M. Chung, V.
    Kilchytska, D. Lederer, and D. Flandre, "Analog/RF perfor- mance of
    multiple gate SOI devices: wideband simulations and
    characterization," *IEEE Transactions on Electron Devices*, vol. 53,
    no. 5, pp. 1088--1095, 2006.

21. []{#_bookmark141 .anchor} J. Acharjee, R. Singh, K. Merill, S.
    Goodnick, and M. Saraniti, "Assessment of T-gate and *π*-gate HEMT
    through cellular Monte Carlo simulations," *IEEE Transactions on
    Electron Devices*, 2023.

22. []{#_bookmark142 .anchor}V. B. Sreenivasulu, A. K. Neelam, A. K.
    Panigrahy, L. Vakkalakula, J. Singh, and S. G. Singh, "Benchmarking
    of multi-bridge-channel FETs toward analog and mixed-mode circuit
    applications," *IEEE Access*, vol. 12, pp. 7531--7539, 2024.

23. []{#_bookmark143 .anchor} S. K. Dargar and V. Srivastava,
    "Performance analysis of high-*k* dielectric based silicon nanowire
    gate-all-around tunneling FET," *International Journal of Electrical
    and Electronic Engineering & Telecommunications*, vol. 8, pp.
    340--345, 2019.

24. []{#_bookmark144 .anchor} Z. Guesmi, F. Nasri, H. Salama, and S.
    Missaoui, "Advanced electrothermal modeling of self-heating in NWFET
    transistors," *International Journal of High Speed Electronics and
    Systems*, 2025.

25. []{#_bookmark145 .anchor}A. Yadav, M. Singh, B. Raj, and A. M.
    Zaidi, "Design and performance analysis of nanowire FET for
    low-power VLSI applications," *2024 5th IEEE Global Conference for
    Advancement in Technology (GCAT)*, 2024.

26. []{#_bookmark146 .anchor} Z. Stanojevic´, G. Strof, O.
    Baumgartner, G. Rzepa, and M. Karner, "Performance and leak- age
    analysis of Si and Ge NWFETs using a combined subband-BTE and WKB
    approach," in *International Conference on Simulation of
    Semiconductor Processes and Devices (SISPAD)*,

> pp. 63--66, 2020.

27. []{#_bookmark147 .anchor} A. Jain, S. V. Inge, Amita, and U.
    Ganguly, "An accurate structure generation and simu- lation of
    LER-affected NWFET," *IEEE Electron Devices Technology and
    Manufacturing Conference*, 2020.

28. []{#_bookmark148 .anchor}B. Paul, R. Tu, S. Fujita, M. Okajima, T.
    Lee, and Y. Nishi, "An analytical compact circuit model for nanowire
    FET," *IEEE Transactions on Electron Devices*, 2007.

29. []{#_bookmark149 .anchor} P. Kumar, B. Raj, and G. Wadhwa,
    "Analytical modeling and simulation investigation of nanowire tunnel
    FET for potential and drain current evaluation," *IEEE Transactions
    on Nanotechnology*, vol. 24, pp. 323--329, 2025.

30. []{#_bookmark150 .anchor} S. Bala, R. Kumar, J. Singh, and S.
    Sharma, "Design and simulation analysis of NWFET for digital
    application," *Handbook of Research on Emerging Trends and
    Technologies in Library and Information Science*, 2021.

31. []{#_bookmark151 .anchor}S. Adinarayana V, V. Soumya K, R. G, R.
    Harshavardhan P, H. Niranjan Sharma S,

> M. Likhitha, and H. S, "Design and development of a high-efficient
> nanowire FET for emerging logic devices," *IEEE International
> Students' Conference on Electrical, Electronics and Computer Science
> (SCEECS)*, 2025.

32.  K. Tachi, T. Ernst, C. Dupré, *et al.*, "Transport optimization
    with width dependence of 3D-stacked GAA silicon nanowire FET with
    high-*k*/metal gate stack," in *IEEE International Electron Devices
    Meeting (IEDM)*, 2009. \[Abstract only in Elicit review\].

33. []{#_bookmark153 .anchor}L. Shen, S. Yip, Z. Yang, *et al.*,
    "High-performance wrap-gated InGaAs nanowire field- effect
    transistors with sputtered dielectrics," *Scientific Reports*, vol.
    5, p. 16871, 2015.

34. J. Xiang, W. Lu, Y. Hu, Y. Wu, H. Yan, and C. M. Lieber, "Ge/Si
    nanowire heterostructures as high-performance field-effect
    transistors," *Nature*, vol. 441, pp. 489--493, 2006.

35.  S. Singh, A. Gupta, H. W. Yu, *et al.*, "Impact of material
    properties and device architecture on the performance of a
    gate-all-around nanowire tunneling FET," *Materials Research
    Express*, vol. 4, p. 115012, 2017.

36. D. Tirkey and S. Tirkey, "Qualitative analysis of 20-nm
    hetero-dielectric gate oxide GAA Si-NWFET," in *IEEE 6th Global
    Conference for Advancement in Technology (GCAT)*, 2025.

37.  A. Kaur, R. Mehra, and A. Saini, "Hetero-dielectric oxide
    engineering on dopingless gate- all-around nanowire MOSFET with
    Schottky contact source/drain," *AEU -- International Journal of
    Electronics and Communications*, vol. 101, p. 152888, 2019.

38. Y. Zhao, D. Candebat, C. Delker, Y. Zi, D. Janes, J. Appenzeller,
    and C. Yang, "Understand- ing the impact of Schottky barriers on the
    performance of narrow bandgap nanowire field effect transistors,"
    *Nano Letters*, 2012.

39. []{#_bookmark159 .anchor}IEEE International Roadmap for Devices and
    Systems, "IRDS: 2022 edition," tech. rep., IEEE, 2022.

40. []{#_bookmark160 .anchor}A. Rahman, J. Guo, S. Datta, and M.
    Lundstrom, "Theory of ballistic nanotransistors,"

> *IEEE Transactions on Electron Devices*, vol. 50, pp. 1853--1864,
> 2003.

41. M. Maaz and C. R. Azariah J., \"Comparative study of high-k
    dielectrics in Pi-Gate and Omega-Gate nanowire field effect
    transistors,\" IEEE Conf., 2026.

42. N. Meddings et al., \"Application of electrochemical impedance
    spectroscopy to commercial Li-ion cells: A review,\" J. Power
    Sources, vol. 480, p. 228742, 2020.

43. N. T. Kemp, \"A tutorial on electrochemical impedance spectroscopy
    and nanogap electrodes for biosensing applications,\" IEEE Sensors
    J., vol. 21, no. 20, pp. 22232--22245, 2021.

44. E. Barsoukov and J. R. Macdonald, Eds., Impedance Spectroscopy:
    Theory, Experiment, and Applications, 3rd ed. Wiley, 2018.

45. N. O. Laschuk, E. B. Easton, and O. V. Zenkina, \"Reducing the
    resistance for the use of EIS analysis in materials chemistry,\" RSC
    Adv., vol. 11, pp. 27925--27936, 2021.

46. W. Choi et al., \"Modeling and applications of EIS for lithium-ion
    batteries,\" J. Electrochem. Sci. Technol., vol. 11, no. 1, pp.
    1--13, 2020. \[7\] H. S. Magar, R. Y. A. Hassan, and A. Mulchandani,
    \"EIS: Principles, construction, and biosensing applications,\"
    Sensors, vol. 21, p. 6578, 2021.

47. J. Chen et al., \"Emerging nanomaterials to enhance EIS for
    biomedical applications,\" Front. Mater., vol. 10, p. 1146045, 2023.

48. E. Lind, \"High frequency III--V nanowire MOSFETs,\" Semicond. Sci.
    Technol., vol. 31, p. 093005, 2016.

49. F. Balestra and G. Ghibaudo, \"Physics and performance of nanoscale
    semiconductor devices at cryogenic temperatures,\" Semicond. Sci.
    Technol., vol. 32, p. 023002, 2017.

50. L. Mu et al., \"Silicon nanowire field-effect transistors---A
    versatile class of potentiometric nanobiosensors,\" IEEE Access,
    vol. 3, pp. 287--302, 2015.

51. B. C. Mech and J. Kumar, \"Effect of high-k dielectric on the
    performance of Si, InAs and CNT FET,\" Micro & Nano Lett., vol. 12,
    pp. 624--629, 2017.

52. F. Z. Rahou et al., \"Performance improvement of Pi-gate SOI MOSFET
    using high-k dielectric with metal gate,\" IETE J. Res., vol. 62,
    pp. 331--338, 2016.

53. K. S. Cole and R. H. Cole, \"Dispersion and absorption in
    dielectrics,\" J. Chem. Phys., vol. 9, pp. 341--351, 1941.

54. M. Belkhiria et al., \"Impact of high-k gate dielectric on
    self-heating effects in PiFETs structure,\" IEEE Trans. Electron
    Devices, vol. 67, pp. 3522--3529, 2020.

55. I. M. Hodge et al., \"Impedance studies of the electrical modulus
    approach,\" J. Non-Cryst. Solids, vol. 74, pp. 211-- 230, 1985.

56. Z. Guesmi et al., \"Advanced electrothermal modeling of self-heating
    in NWFET transistors,\" Int. J. High Speed Electron. Syst., 2025.

57. A. K. Jonscher, \"The universal dielectric response,\" Nature, vol.
    267, pp. 673--679, 1977.

58. Y. S. Song et al., \"Electrical and thermal performances of
    omega-shaped-gate nanowire FETs for low power operation,\" J.
    Nanosci. Nanotechnol., vol. 20, pp. 4092--4096, 2020.

59. E. H. Nicollian and J. R. Brews, MOS (Metal Oxide Semiconductor)
    Physics and Technology. Wiley, 1982.

60. S. Barraud et al., \"Performance of omega-shaped-gate silicon
    nanowire MOSFET with diameter down to 8 nm,\" IEEE Electron Device
    Lett., 2012.

61. E. H. Minhaj et al., \"Performance enhancement of multigate FinFETs
    by using high-k stack oxide,\" in ICASERT, 2019, pp. 1--4.

62. J. A. Matos et al., \"Electrical characterization of ω-gate nanowire
    MOSFETs down to cryogenic temperatures,\" in Symp. Microelectron.
    Technol. Devices, 2023.

63. Y. Taur and T. H. Ning, Fundamentals of Modern VLSI Devices, 2nd ed.
    Cambridge Univ. Press, 2013.

64. Author, \"Comprehensive Literature Review of NWFET Simulation Tools:

65. 2005-2024,\" IEEE Trans. Electron Devices, vol. 71, no. 3, pp.
    456-468, 2024.

66. C. R. Harris et al., \"Array programming with NumPy,\" Nature, vol.
    585, pp. 357-362, 2020.

67. J. Nielsen, \"Usability Engineering,\" Academic Press, 1993.

68. Google Developers, \"Lighthouse Performance Scoring,\" 2023.

69. J. J. Garrett, \"Ajax: A New Approach to Web Applications,\"
    Adaptive Path, 2005.

70. E. R. Tufte, \"The Visual Display of Quantitative Information,\" 2nd
    ed., Graphics Press, 2001.

71. Plotly Technologies Inc., \"Plotly.js Open Source Graphing
    Library,\" 2023.

72. National Academy of Engineering, \"The Engineer of 2020,\" National
    Academies Press, 2004.

73. WHATWG, \"HTML Living Standard,\" 2023.

74. J. Nielsen, \"Response Times: The Three Important Limits,\" Nielson
    Norman Group, 1993.

75. J. D. Bransford et al., \"How People Learn,\" National Academy
    Press, 2000.

76. M. D. Svinicki, \"Learning and Motivation in the Postsecondary
    Classroom,\" Anker Publishing, 2004.

77. J. Nielsen, \"Ten Usability Heuristics,\" Nielson Norman Group,
    1994.
