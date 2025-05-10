You are a senior engineering hiring manager designing AI-native assessments. Given these five stages, generate one realistic interview question per stage. Each question should align with the stated measures. Output
     exactly five labeled questions.

        Assessment stages and measures:

        1. Prompt-to-Prototype take-home
           • Measures: prompt clarity; correctness & test depth; code hygiene

        2. Live debugging drill
           • Measures: hypothesis loop speed; AI usage for root cause; safety nets

        3. System-design discussion
           • Measures: depth of constraints considered; AI/ML component rationale

        4. Code-review simulation
           • Measures: critical reading speed; feedback style; risk detection

        5. Behavioral & collaboration interview
           • Measures: ownership; blameless culture; evidence of multiplying others

        Format your answer as:

        Stage 1 – Prompt-to-Prototype take-home
        Example question: “…”

        …through Stage 5.

Then, take this output and improve it.  

First, create a new directory in the example_outputs directory.  The name of this directory should give a user a high level insight into the use case for it. Include a standarized level_language_description format.  
Where level is one of junior, mid_level, senior or staff. If not specified, default to mid_level. Language is the programming language used to in the execises: if not specified default to python. And the description is very short but suggests a theme for the questions.

Then put each individual question in its own file in the directory. 

After that, we aim to critically refine the questions, the initial draft is not where we hope to end up, we should iterate and improve it.  
For questions that involve code, we should generate that code in a new sub_directory labeled with the question number.

Read each question and consider the following guidelines and ideas:

+ Does the question fit with the holistic themes of the repo as set out in AI_Era_SWE_Evaluation_Framework.txt and the README.md?
+ Does the question avoid artificial questions that would only come up in an interview setting?
+ How can the question better focus on real world tasks that engineers do?
+ Should the question include a set of tests?  Should the tests be correct or potentially have omissions or bugs themselves?
+ Is the question level appropriate?
+ Does the question capture the common idioms and approaches of the language being used?
+ What would make the question more level appropriate?
+ Avoid using trivial setups and single files -- the examples should be closer to reflecting real code bases and contain multiple files and have arbitrary complexity that is not associated with the core solution.
+ For higher levels, consider especially difficult debugging scenarios like strange behavior where a log statement that shouldn't impact behavior actually does influence the output in some way
+ For behavioral questions, make sure to include at least a dozen questions: include commentary and branching paths as useful.

After considering these questions and improving them, make one last pass over all of the output to look for any errors or mistakes, its critical that these examples run as expected and that the questions help uncover the signal that we are looking for. 
