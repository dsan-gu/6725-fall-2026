# Syllabus - DSAN 6725 Applied Generative AI for Developers

**Professor**: Amit Arora
**Email**: TBD
**Class Time**: Tuesdays 9:30 AM - 12:00 PM
**Classroom**: Intercultural Center 107
**First Class**: January 13, 2026, 9:30 AM - 12:00 PM

**Office Hours**:

Professor's Office hours are by appointment only. Please use the following links to book appointments. If none of these times work for you, please email me to make appointments.

| Appointment | Day | Time | Link |
|------------|-----|------|------|
| Virtual | Wednesday | 5:00 PM - 6:00 PM | TBD |

*This syllabus is subject to change at any time.*

## Teaching Assistants (TA)

**Name**: Zixu "Michael" Hao
**Email**: zh301@georgetown.edu
**Office Hours**: Mondays 2:00 PM - 3:00 PM, Fridays 2:00 PM - 3:00 PM

## Textbooks

There is no required textbook for the course. However, you can consider the following if you like:

- [Hands-On Large Language Models: Language Understanding and Generation](https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961/ref=sr_1_1?crid=2L8JBIHIZUKO1&dib=eyJ2IjoiMSJ9.y8jTOKNtfaF-RUePWCWwsdnAIo4v5YE_XE2TIlLVQCBGA6Q716R03HVJHfrq-uS1.J-n8l0ZZvrzb7ARZx8p_xTnaPW7Za1bED91saKrAKlE&dib_tag=se&keywords=Hands-On+Large+Language+Models%3A+Language+Understanding+and+Generation&qid=1734626165&s=books&sprefix=hands-on+large+language+models+language+understanding+and+generation+%2Cstripbooks%2C98&sr=1-1)
- [Generative AI Foundations in Python: Discover key techniques and navigate modern challenges in LLMs](https://www.amazon.com/Generative-Foundations-Python-techniques-challenges/dp/1835460828) chapters 5, 6, 7 and 8.

We may also provide supplemental materials (articles, links, videos, etc.) to complement the readings.

**You must read assigned readings prior to the lectures.**

## Prerequisites

- Experience with Python and invoking REST APIs.
- Experience with git and GitHub

Some tutorials to brush up on these skills:

- [git - the simple guide](http://rogerdudler.github.io/git-guide/)
- [Python and REST APIs: Interacting With Web Services](https://realpython.com/api-integration-in-python/)
- [Nico Riedmann's Learn git concepts, not commands](https://dev.to/unseenwizzard/learn-git-concepts-not-commands-4gjc)
- [Python course](https://github.com/gitdagray/python-course/tree/main)

## Course Description

Applied Generative AI for developers is a graduate-level course that provides students with a deep understanding of building generative AI applications. This course is designed for AI developers aiming to build cutting-edge Generative AI (GenAI) applications. Focusing on the applied side of AI, students will explore key techniques such as in-context learning (ICL), retrieval-augmented generation (RAG), AI agents, and responsible AI principles.

The course covers advanced tools and methods, including embedding models, inference optimizations (e.g., quantization, multi-adapter swapping), fine-tuning of pre-trained models and benchmarking LLMs. Students will gain hands-on experience with open-source tools like LangChain, LlamaIndex, and platforms such as AWS, applying their skills in practical GenAI applications. The course culminates in a capstone project, preparing participants to deploy scalable, optimized AI systems in real-world scenarios. This course bridges the gap between data science knowledge and applied AI development, empowering students to solve industry-level challenges.

## Technology Inventory

This course uses Python as the primary programming language. Students will work with:

- **Python 3.11+**: Primary development language
- **Cloud Platforms**: Amazon Web Services (AWS) for cloud-based development and deployment
- **Gen AI Tools**: LangChain, LlamaIndex, Amazon Bedrock
- **Development Tools**: git, GitHub, Docker, uv (Python package manager)
- **AI Models**: Large Language Models (LLMs), embedding models

## Course Website

*Please use Canvas for all class information, requirements, due dates, deliverables, and submissions.*

Review all Announcements and Modules.

The course will use Canvas, https://canvas.georgetown.edu/. Announcements, homework assignments and solutions, course material such as documentation, links, data sets and code will all be posted there. You can look up your grades, and online surveys will also be conducted here. Students in this course are required to visit this page once a day. Announcements will usually only appear on the webpage. You will also have to access data sets on the Internet and need to be comfortable with this.

**In addition**: GitHub Classroom will be used for all assignment and lab submissions.

**Communication**: The primary mode of communication is Slack. Please join the class Slack channel [here](https://join.slack.com/t/dsan6725appli-imy3613/shared_invite/zt-3mh6xismt-sKHNzqXmFrJV5ztgueAPbA).

## Cloud Resources

You will use cloud resources on [Amazon Web Services](http://aws.amazon.com). We will discuss how to set up your accounts and environments in class and lab within the first couple of weeks. You will get credits on both platforms that will be enough to support your coursework throughout the semester.

!!! warning "Managing cloud resources"
**IT IS YOUR RESPONSIBILITY TO MANAGE THE CREDITS AND RESOURCES PROVIDED TO YOU. YOU MUST SHUT DOWN YOUR CLOUD RESOURCES WHEN NOT IN USE.**

## Course Calendar and Topics

### Learning Objectives

By the end of this course, students will be able to:

1. Build GenAI applications with prompt engineering, RAG and AI Agents
2. Fine-tune LLMs
3. Apply Responsible AI principles
4. Optimize inference for deploying apps at scale
5. Complete a comprehensive capstone project

A Google Spreadsheet overview of the course with topics, dates, and deliverables is available and will be updated along with the individual pages in Canvas.

| Week  | Module                                               | Details                                                                                                  |
|-------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1     | Introduction to Generative AI and Coding Assistants  | Overview of course objectives, introduction to GenAI, and AI-powered coding tools                    |
| 2     | In-context Learning                           | Introduction to prompt engineering |
| 3     | Retrieval Augmented Generation (RAG)         | Build Q&A systems using vector databases, foundation models, graph RAG, and advanced RAG techniques including chunking strategies and query rewrites              |
| 4     | Model Context Protocol (MCP) Servers                     | Building MCP servers for tool integration, API wrapping, authentication, and deployment patterns (local and remote)
| 5     | Agent-Based Architectures - Part 1                                  | Tool usage, build agents with LangChain, LlamaIndex and Amazon Bedrock      |
| 6     | Agent-Based Architectures - Part 2                                  | Multi-agent collaboration and memory management       |
| 7     | Gen AI app best practices and Observability                                   | Best practices for deploying GenAI apps in production with monitoring and evals           |
| 8     | Guardrails and Evaluation of Generative Models                                        | Data security, guardrails, ethics, bias mitigation, and evaluation frameworks
| 9     | Benchmarking and Performance Analysis        | Price, performance and accuracy benchmarking using open-source tools |
| 10    | Embeddings Models and Representation Learning                      | Background on vector embeddings, fine-tuning embeddings models                             |
| 11    | Model serving and Optimizations                                     | Inference servers, engines, speculative decoding, quantization, distillation, adapter swapping        |
| 12    | Fine-tuning Generative AI models         | Fine-tune LLMs with custom data using LoRA, PEFT, and other techniques            |
| 13    | Gen AI platform design, open-discussion            | How to build a platform and not just apps     |
| 14    | Project presentation, open-discussion                             | Final project presentations and open discussion on course topics                                        |

## Final Grades

### Grading Weights

| Deliverable | Final Weight Percentage |
|------------|------------------------|
| Group Project | 40% |
| Homework Assignments | 30% |
| Lab Completions | 20% |
| Quizzes | 10% |

**Total: 100%**

### Grading Scale

- A: >= 92.5
- A-: 89.5 - 92.49
- B+: 87.99 - 89.49
- B: 81.5 - 87.98
- B-: 79.5 - 81.49

We have no plans to curve the final grade.

## Learning Activities

This is a hands-on, practical, workshop-style course that provides opportunities to use the tools and techniques discussed in class. Although this is not a programming course per se, there is a lot of programming involved.

### Lectures and Labs

The course is split into a lecture/lab format. During the lecture, we will discuss the concepts and techniques for building Gen AI apps on cloud platforms. During the lab sessions, you will be completing exercises and following examples which are designed to show you how to implement the ideas and concepts with various tools.

We will start the labs in class but we will not finish. It is your responsibility to complete the labs (which is part of the grade) and will enable your learning. Lectures may not cover all the material and some topics will be introduced in the lab or through readings/assignments.

### Readings

On certain weeks, readings will be assigned to prepare you for the lecture material being presented. These readings should take an hour or less per week.

### Quizzes

There will be 6 quizzes per semester. Quizzes ensure you are keeping up with the material presented in the class. Quizzes are meant to be brief and low-stress with a time limit of 5-10 minutes. The material will be drawn from lectures, labs, and readings.

### Lab Deliverables

Each lab will have a deliverable that is due by the next lecture. It is essential that you learn the skills presented in the labs so that you can effectively complete the assignments and the capstone project. Time will always be given for the lab deliverables to be completed during lab, however, it is your responsibility to complete the deliverable as part of your work outside of lecture/lab time.

### Homework Assignments

You will be given several homework assignments for roughly half of the semester. The goal of these problem sets is to enhance your GenAI application development skills. The problem sets will build on the labs and will be much more in-depth. Deliverables from the assignment will usually include code written for your programs and the output produced.

**Important Note**: We reuse problem set questions, we expect students not to copy, refer to, or look at the solutions in preparing their answers. Since this is a graduate-level class, we expect students to want to learn and not search online for answers. See Academic Integrity section.

!!! warning "Start early on the assignments"
**Please start assignments as soon as they are posted. These assignments can take several hours to complete depending on your familiarity with the material. You will not complete the assignments on time if you start the day they are due.**

### Discussions

There will be discussion posts where you communicate with your peers about course topics and your project. Individual project plans will be communicated and discussed on the discussions. You will communicate progress on your project to the discussion board and get feedback. This feedback will be incorporated into future discussion posts.

### Capstone Project

The capstone project is a significant component of this course where students will apply the skills learned throughout the semester to build a production-ready GenAI application. Details will be provided in the first few weeks of class.

## Grading and Evaluation

Many of the assignments you will work on are open-ended. Grading is generally holistic, meaning that there will not always be specific point values for individual elements of a deliverable. Each deliverable submission is unique and will be compared to all other submissions.

- If a deliverable exceeds the requirements and expectations, that is considered A level work.
- If a deliverable just meets the requirements and expectations, that is considered A-/B+ level work.
- If a deliverable does not meet the requirements, that is considered less than B level of work.

All deliverables must meet the following general requirements, in addition to the specific requirements of each deliverable:

If your submission meets or exceeds the requirements, is creative, is well thought-out, has proper presentation and grammar, and is at the graduate student level, then the submission will get full credit. Otherwise, partial credit will be given and deductions may be made for any of the following reasons:

**Points will be deducted for any of the following reasons:**

- The instructions are not followed
- There are missing sections of the deliverable
- The overall presentation and/or writing is sloppy
- There are no comments in your code
- There are files in the repository other than those requested
- There are absolute filename links in your code
- The repository structure is altered in any way
- Files are named incorrectly (wrong extensions, wrong case, etc.)

## Submission Details

### GitHub classroom

We use GitHub Classroom for all class deliverables: assignments, labs, and the final project. Submitting your work is the process of committing your files and results to your local repository **and** then pushing it to GitHub.

#### Use the `final-submission` commit message

When you are ready for your work to be evaluated, you **MUST** use the commit message `final-submission`. If you do not use the commit message `final-submission` we will assume that you are still working in the repository and we will only grade what is present. By submitting that commit message, you are stating that you are finished with the assignment and are ready for feedback.


In case you need to make a correction after your `final-submission` **and** the submission deadline has not yet passed, then you can *amend* your previous commit.  See [amending a commit](https://www.atlassian.com/git/tutorials/rewriting-history) for instructions. **Do not change the commit message,** it should continue say "final-submission" after the amend.

!!! warning "No modifications after final-submission"
**No further edits to your GitHub repository are allowed after using the `final-submission` commit message.**

!!! note "How we detect late submissions"
We will use **commit datetime** and **commit message** to assess lateness. 


### Late Policy

There are no extensions to due dates unless there are extraordinary circumstances, and those will be determined on a case-by-case basis. If you miss a deliverable entirely, you will receive a grade of 0 (zero).

We realize life gets in the way sometimes and you may not be able to complete an assignment on time. Therefore, all deliverables can be up to 24 hours late with NO PENALTY (24 hours grace period for submission). That means students (groups) can upload the assignment up to 24 hours later than the posted due date and will receive credit for correct answers without any point reductions (only up to 24hrs after the due date/time). Any assignment submitted after the grace period will result in reduction of points as follows.

**After 24 hours, the penalty is set at the following schedule:**

- Homework Assignments: -5% per day for up to 5 days
- Lab Deliverables: -5% per day for up to 5 days
- Discussions: -10% per day for up to 5 days
- Project Intermediate Assignments: -15% per day for up to 5 days

**This does not apply to the final project.** The final project presentation and deliverables CANNOT be late for any reason.

**This does not apply to quizzes.** Missed in-class quizzes cannot be made up and will receive a grade of zero unless there is an extenuating circumstance.


## Class Communication

Always use email or Slack as the primary communication methods.

**Slack Guidelines:**

- All announcements will be posted on Canvas and Slack
- Use Slack for any question you may have about the course, about assignments or any technical issue. This way everyone can learn from each other's questions. We will be monitoring and providing answers on a regular basis.
- Individual emails containing any course question that is not personal will not be answered
- Slack DMs are not to be used **unless** we DM you first and you can respond to our message. Students may not initiate DMs.
- Keep an eye on the questions posted in Slack. Use the search function. It's very possible that we have already answered a question, and we reserve the right to point you to the syllabus, previous Slack messages, or other document containing the information requested
- Assignment, lab and project questions will only be answered on Slack up to 12 hours before something is due

## Academic Integrity and Collaboration - ZERO TOLERANCE POLICY

All students are expected to maintain the highest standards of academic and personal integrity in pursuit of their education at Georgetown. Academic dishonesty in any form is a serious offense, and students found in violation are subject to academic penalties that include, but are not limited to, zero'ing out assignments, reduced grade, failure of the course, termination from the program, and revocation of degrees already conferred. All students are held to the Georgetown University Honor Code. For more information about the Honor Code see https://honorcouncil.georgetown.edu/.

**We have a ZERO TOLERANCE POLICY and if students are found to be in violation there will be consequences and the students will be penalized and reported.**

### Rules

- All individual deliverables in this course are individual work, which means INDIVIDUAL.
- All submitted code must be your own. This will be verified for every deliverable against every submission, and any similarity greater than 60% will be considered to be unauthorized collaboration.
- We have had issues with students sharing code files with others and that are then submitted by multiple students as unique individual submissions. This is totally unacceptable and will result in penalties to all students involved.
- If you have referred to lecture codes or resources on the internet please specify the references.
- All other deliverables must be your own as well.

**The following collaboration and communication is allowed and encouraged in Canvas discussion Q&A boards, labs, and office hours:**

- The discussion of ideas and approaches to problems
- The discussion and resolution of any technical issue

## Use of Generative AI Tools

We recognize the recent availability of very powerful generative AI tools like ChatGPT, GitHub Copilot, and others. These tools can help us be more effective and we embrace their use.

**You are allowed to use GenAI tools in a non-substantial way.**

What does non-substantial mean? **It means that whatever is generated by GenAI must not make up the majority of the work you do.**

Any use of these tools must abide by the following rules:

- You must acknowledge the use of GenAI tools
- You must comment which code blocks were generated by GenAI
- You must note which written sections were generated by GenAI
- If you used a prompt to ask the GenAI tool to do something, you must include it

**For this course, valid uses of GenAI can be:**

- Generating a code snippet or single function to perform a task (you'll likely need to modify it anyway)
- Commenting code
- Using it as a writing aid (spelling, grammar, word choice, limited phrase translation) on content created by you, not the actual writing
- Generating visualization starter code (you can accelerate the generation of the starting point, but you still need to customize it)

!!! warning "Academic integrity"
Any deviation from these rules is considered a violation of academic integrity and will be acted on. You typically KNOW when you are crossing the line into unethical territory. As a general rule, if you feel like you might be crossing a line, then you probably are!

In addition to what we are stating here, please take a look at the [Data Science and Analytics Program's ChatGPT usage guidelines](https://gu-dsan.github.io/5200-spring-2024/site-page-content/DSAN-ChatGPT-usage-guidelines.pdf).

## University Policies and Support Services

### Georgetown University’s Plagiarism Policy 

Plagiarism or academic dishonesty in any form will not be tolerated and may result in a failing grade. All Honor Code violations will be submitted to the Honor Council. 

Academic integrity is central to the learning and teaching process. Students are expected to conduct themselves in a manner that will contribute to the maintenance of academic integrity by making all reasonable efforts to prevent the occurrence of academic dishonesty. Academic dishonesty includes (but is not limited to) obtaining or giving aid on an examination, having unauthorized prior knowledge of an examination, doing work for another student, and plagiarism of all types, including copying code. 

Plagiarism is the intentional or unintentional presentation of another person’s idea or product as one’s own. Plagiarism includes, but is not limited to the following: copying verbatim all or part of another’s written work; using phrases, charts, figures, illustrations, code, or mathematical/scientific solutions without citing the source; paraphrasing ideas, conclusions, or research without citing the source; and using all or part of a literary plot, poem, film, musical score, or other artistic product without attributing the work to its creator. Students can avoid unintentional plagiarism by following carefully accepted scholarly practices. Notes taken for papers and research projects should accurately record sources cited, quoted, paraphrased, or summarized sources and articles should be acknowledged in footnotes. 

### Honor System

All students are expected to maintain the highest standards of academic and personal integrity in pursuit of their education at Georgetown. Academic dishonesty, including plagiarism, in any form, is a serious offense, and students found in violation are subject to academic penalties that include, but are not limited to, failure of the course, termination from the program, and revocation of degrees already conferred. All students are held to the Georgetown University Honor Code. For more information about the Honor Code [http://gervaseprograms.georgetown.edu/honor/](http://gervaseprograms.georgetown.edu/honor/) 

### Academic Integrity and Courtesy 

As a Jesuit, Catholic university committed to the education of the whole person, Georgetown expects all members of the academic community, students and faculty, to strive for excellence in scholarship and in character. The University spells out the specific minimum standards for academic integrity in its Honor Code and the procedures to be followed if academic dishonesty is suspected. Over and above the honor code, in this course, we will seek to create an engaged and passionate learning environment characterized by respect and courtesy in both our discourse and our ways of paying attention to one another. 

### Academic Resource Center

[The Academic Resource Center (ARC)](https://academicsupport.georgetown.edu/) is the campus office responsible for reviewing medical documentation and determining reasonable accommodations for students with disabilities. You can reach the ARC via email at [arc@georgetown.edu.](mailto::arc@georgetown.edu)

### Counseling and Psychiatric Services (CAPS) 

As Georgetown faculty, you are among the most important individuals in some of the students’ lives. They may turn to you when they are struggling and in times of need, or you may be one of the first to notice when they are distressed. 

The CAPS website has tips for faculty on how to deal with struggling or distressed students. 
202.687.6985 or after hours, call (833) 960-3006 to reach Fonemed, a telehealth service; individuals may ask for the on-call CAPS clinician. 

### Emergency Preparedness and HOYAlert
We encourage all faculty to become familiar with Georgetown’s Office of Emergency Management and sign up for HOYAlert to receive important safety and University operating status updates. Faculty teaching at the Georgetown Downtown campus might also want to sign up for AlertDC to obtain safety and traffic updates. 

### Office of Institutional Compliance and Ethics

The Office of Institutional Compliance and Ethics supports and coordinates many compliance-related activities the University undertakes. With the endorsement and assistance of the University’s senior leadership, this Office is responsible for leading the development, implementation, and operation of the Georgetown Institutional Compliance and Ethics Program. 

### Office of Institutional Diversity, Equity and Affirmative Action (IDEAA)

The mission of IDEAA is to promote a deep understanding and appreciation among the diverse members of the University community to result in justice and equality in educational, employment, and contracting opportunities, as well as to lead efforts to create an inclusive academic and work environment. 

### Title IX/Sexual Misconduct 

Georgetown University and its faculty are committed to supporting survivors and those impacted by sexual misconduct, which includes sexual assault, sexual harassment, relationship violence, and stalking. Georgetown requires faculty members unless otherwise designated as confidential, to report all disclosures of sexual misconduct to the University Title IX Coordinator or a Deputy Title IX Coordinator. Suppose you disclose an incident of sexual misconduct to a professor in or outside of the classroom (except disclosures in papers). In that case, that faculty member must report the incident to the Title IX Coordinator or Deputy Title IX Coordinator. The coordinator will, in turn, reach out to the student to provide support, resources, and the option to meet—[Please note that the student is not required to meet with the Title IX coordinator.]. More information about reporting options and resources can be found on the [Sexual Misconduct Website.](https://sexualassault.georgetown.edu/resourcecenter)

If you would prefer to speak to someone confidentially, Georgetown has a number of fully confidential professional resources that can provide support and assistance. These resources include:

* Health Education Services for Sexual Assault Response and Prevention: confidential email sarp@georgetown.edu
* Counseling and Psychiatric Services (CAPS): 202.687.6985 or after hours, call (833) 960-3006 to reach Fonemed, a telehealth service; individuals may ask for the on-call CAPS clinician 

_Title IX Sexual Misconduct Statement_ Please know that as faculty members, we are committed to supporting survivors of sexual misconduct, including relationship violence and sexual assault. However, university policy also requires us to report any disclosures about sexual misconduct to the Title IX Coordinator, whose role is to coordinate the University’s response to sexual misconduct. 

Georgetown has a number of fully confidential professional resources who can provide support and assistance to survivors of sexual assault and other forms of sexual misconduct. These resources include:

* [Getting Help](https://sexualassault.georgetown.edu/get-help/#)
* Jen Schweer, MA, LPC<br/>Associate Director of Health Education Services for Sexual Assault Response and Prevention (202) 687-0323<br/>[jls242@georgetown.edu](mailto:jls242@georgetown.edu) 
* Erica Shirley, Trauma Specialist<br/>Counseling and Psychiatric Services (CAPS)<br/>(202) 687-6985<br/>[els54@georgetown.edu](mailto:els54@georgetown.edu) 

### Threat Assessment

Georgetown University established its Threat Assessment program as part of an extensive emergency planning initiative. The program at Georgetown has been developed and implemented to meet current best practices and national standards for hazard planning in higher education institutions and workplace violence prevention. 

### Special Accommodations 

If you believe that you have a disability that will affect your performance in this class, don’t hesitate to get in touch with the [Academic Resource Center](mailto:arc@georgetown.edu) for further information. The center is located in the Leavey Center, Suite 335. The Academic Resource Center is the campus office responsible for reviewing documentation provided by students with disabilities and determining reasonable accommodations according to the Americans with Disabilities Act (ADA) and University policies. 
