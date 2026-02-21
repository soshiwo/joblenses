def get_assessment_data():
    return [
        {
            "id": "s1",
            "title": "The Boardroom Discrepancy",
            "text": "You are finalizing the annual DEI compensation report for the Board of Directors, scheduled to present in 30 minutes. While running a final sanity check, you discover a subtle logic error in your SQL join that incorrectly inflated the pay parity metric by 2%. The report currently shows you hit your targets, but the true data shows a miss. Fixing and rerunning the pipeline will take an hour, causing you to miss the meeting and delaying the board's vote on executive bonuses.",
            "opts": [
                {"t": "Pull the report, explain the data error to the board, and ask for a delay to ensure complete accuracy.", "s": [10, 0, 0, 0, 10]},
                {"t": "Present the report but verbally disclose the 2% variance during the meeting, promising an updated data addendum.", "s": [5, 0, 5, 10, 0]},
                {"t": "Present the report as-is to secure the executive bonus vote, then quietly deploy a hotfix for all future reporting.", "s": [0, 0, 0, 10, 0]},
                {"t": "Mad-dash to write a quick Python script to patch the compiled data in memory, risking an untested, undocumented fix.", "s": [0, 10, 0, 5, 0]}
            ]
        },
        {
            "id": "s2",
            "title": "The GDPR Executive Override",
            "text": "The newly hired Chief Revenue Officer (CRO) demands a highly granular dashboard mapping individual sales performance directly to health leave and Employee Assistance Program (EAP) usage to 'identify weak links.' This crosses severe GDPR and internal privacy boundaries, but the CRO has the CEO's backing and threatens to freeze your team's software budget if you don't deliver by the end of the week.",
            "opts": [
                {"t": "Refuse the request outright citing GDPR law and escalate the attempted privacy breach to the Legal and Compliance team.", "s": [10, 0, 0, 0, 10]},
                {"t": "Create a highly aggregated, anonymized version of the dashboard that shows macro trends without exposing individual identities.", "s": [5, 10, 0, 10, 5]},
                {"t": "Build exactly what the CRO asked for; they explicitly own the legal risk, and your team desperately needs the budget.", "s": [0, 0, 0, 10, 0]},
                {"t": "Collaborate with the CRO's chief of staff to understand the root business problem and offer a safer, alternative sales-enablement metric.", "s": [5, 0, 10, 5, 0]}
            ]
        },
        {
            "id": "s3",
            "title": "The Legacy Labyrinth vs. Python Pioneer",
            "text": "Your People Analytics team is drowning in legacy Excel macros. You've secretly spent your weekends building a fully automated, scalable Python/Airflow data pipeline. It works perfectly, but the rest of your team only knows Excel and VBA. Implementing it immediately will skyrocket the team's output but will completely alienate your peers and create a single point of failure (you) for maintaining it.",
            "opts": [
                {"t": "Deploy the pipeline immediately to drastically improve output, telling the team they need to upskill to Python or be left behind.", "s": [0, 10, 0, 10, 0]},
                {"t": "Delete your Python work and help the team incrementally improve the existing Excel macros so everyone stays comfortable and aligned.", "s": [0, 0, 10, 0, 5]},
                {"t": "Propose a phased rollout where you run the Python pipeline in parallel while running weekly lunch-and-learns to teach the team Python.", "s": [5, 10, 10, 5, 5]},
                {"t": "Keep using the Python script secretly to finish your own work faster, leaving the team to their manual processes.", "s": [0, 0, 0, 10, 0]}
            ]
        },
        {
            "id": "s4",
            "title": "The Hoarded Analytics Holy Grail",
            "text": "Your most brilliant but abrasive junior data scientist has developed a groundbreaking predictive model for quality-of-hire. However, they refuse to document their code, hoard the repository access, and belittle colleagues who ask questions. The business now relies heavily on their monthly outputs to make critical hiring decisions.",
            "opts": [
                {"t": "Issue a final warning or fire them. Toxic behavior destroys the team culture, even if it hurts short-term business results.", "s": [10, 0, 10, 0, 5]},
                {"t": "Tolerate the behavior. The business impact of the model is simply too high to risk losing the employee right now.", "s": [0, 0, 0, 10, 0]},
                {"t": "Pair them with a senior engineer for a mandatory 'code refactoring sprint' disguised as a mentorship program to extract the knowledge.", "s": [5, 5, 5, 10, 0]},
                {"t": "Lock their repository access until they provide full documentation and host a team-wide knowledge-sharing session.", "s": [10, 0, 5, 0, 10]}
            ]
        },
        {
            "id": "s5",
            "title": "The Predictive Attrition Panic",
            "text": "Your newly launched machine learning model predicts employee attrition. The CHRO wants the data immediately to hand out pre-emptive retention bonuses to top-flight risks. However, you've noticed the model disproportionately flags employees who recently returned from maternity leave as 'high risk,' indicating a dangerous algorithmic bias. The CHRO says, 'We don't have time to tune it, just give me the top 50 names.'",
            "opts": [
                {"t": "Hand over the list. The CHRO makes the final call on compensation, and retaining top talent is the current business priority.", "s": [0, 0, 0, 10, 0]},
                {"t": "Refuse to provide the list and shut down the model entirely until the bias is mathematically and ethically eradicated.", "s": [10, 0, 0, 0, 10]},
                {"t": "Provide the list but manually filter out all recent maternity returnees to temporarily bandage the bias issue without delaying the bonuses.", "s": [5, 0, 0, 10, 5]},
                {"t": "Work overnight to write a post-processing algorithm that mathematically neutralizes the leave-status weights, delivering a safe list by morning.", "s": [10, 10, 0, 10, 5]}
            ]
        },
        {
            "id": "s6",
            "title": "The Ghost in the HRIS Machine",
            "text": "You wrote a complex API integration to sync your analytics data warehouse with the core HRIS. Due to a mapping error you missed, the script accidentally downgraded the job architecture tiers for 200 employees, which might affect their upcoming automated payroll run. Nobody has noticed yet. Reversing it requires confessing the catastrophic error to the CIO and CHRO, potentially costing you your job.",
            "opts": [
                {"t": "Immediately alert the CIO, CHRO, and Payroll, taking full ethical responsibility and providing a step-by-step rollback plan.", "s": [10, 0, 10, 0, 10]},
                {"t": "Quietly write a reverse-script to fix the data in the middle of the night and erase the system logs to cover your tracks.", "s": [0, 10, 0, 10, 0]},
                {"t": "Fix the data quietly but leave the logs intact, hoping nobody ever runs an audit on that specific timeframe.", "s": [0, 5, 0, 10, 0]},
                {"t": "Blame the vendor API for the sudden data shift and submit an 'emergency vendor patch' to restore the tiers without taking blame.", "s": [0, 0, 0, 10, 0]}
            ]
        },
        {
            "id": "s7",
            "title": "The M&A Data Room Dilemma",
            "text": "During a hostile corporate takeover, the acquiring company's aggressive consulting firm demands raw, unanonymized employee pulse survey data, including free-text comments, to 'identify cultural detractors.' You promised employees total anonymity when they took the survey. The M&A deal hinges on transparency, and your CEO orders you to upload the raw file to the data room immediately.",
            "opts": [
                {"t": "Upload the file. The CEO's direct orders and the financial success of the M&A override a survey disclaimer.", "s": [0, 0, 0, 10, 0]},
                {"t": "Quit on the spot or refuse outright rather than violate the ethical promise of anonymity you made to the employees.", "s": [10, 0, 0, 0, 10]},
                {"t": "Strip the names but leave the raw comments and demographic tags, hoping the consultants can't reverse-engineer the identities.", "s": [5, 0, 0, 10, 0]},
                {"t": "Use an NLP script to summarize the comments into thematic, aggregated insights, refusing the raw text while still delivering the analysis.", "s": [10, 10, 0, 5, 10]}
            ]
        },
        {
            "id": "s8",
            "title": "The Agile Evangelist's Dilemma",
            "text": "You are driving a massive transformation from static reporting to predictive analytics. The existing HR reporting team is terrified of losing their jobs and is actively passively-aggressively sabotaging your project by imposing endless, unnecessary data validation checks that delay your sprints by weeks. The executive sponsor expects the new platform live by Q3.",
            "opts": [
                {"t": "Escalate their insubordination to leadership and request the reporting team be formally reprimanded or reassigned so you can hit your deadline.", "s": [0, 10, 0, 10, 0]},
                {"t": "Pause the predictive analytics rollout entirely to focus purely on change management and making the legacy team feel safe.", "s": [0, 0, 10, 0, 5]},
                {"t": "Carve out a safe 'shadow environment' where the legacy team can run their old checks against your new data, while you push the main platform live.", "s": [5, 10, 5, 10, 5]},
                {"t": "Surreptitiously bypass their validation checks entirely, deploying the platform and proving its accuracy to executives after the fact.", "s": [0, 10, 0, 10, 0]}
            ]
        },
        {
            "id": "s9",
            "title": "The Promotion Algorithm Audit",
            "text": "A close colleague who is up for a massive promotion built a 'talent matching' algorithm that is saving the company millions. While reviewing their code to learn their technique, you realize the algorithm severely penalizes employees who utilize flexible working hours, disproportionately affecting working parents. If you report this, the algorithm will be scrapped, and your friend will lose the promotion.",
            "opts": [
                {"t": "Report the bias immediately to the Head of People Analytics and Legal, halting the algorithm's use.", "s": [10, 0, 0, 0, 10]},
                {"t": "Confront your friend privately, giving them 48 hours to fix the model and claim it was a 'planned iterative update' before you escalate.", "s": [5, 0, 10, 5, 5]},
                {"t": "Keep quiet. The company is saving millions, and you don't want to destroy your friend's career over a statistical weighting issue.", "s": [0, 0, 10, 10, 0]},
                {"t": "Secretly commit a patch to their repository that lessens the penalty for flexible hours without telling them.", "s": [0, 10, 0, 5, 0]}
            ]
        },
        {
            "id": "s10",
            "title": "The Executive Dash of Illusions",
            "text": "The COO wants a real-time 'Return to Office Productivity' dashboard. They want badge-swipe data correlated directly with keyboard-stroke monitoring and lines of code committed, displayed on a leaderboard in the office lobby. This borders on illegal under European Works Council agreements and creates a draconian culture, but the COO is adamant it will 'drive a high-performance culture.'",
            "opts": [
                {"t": "Build it exactly as requested. The COO sets the culture and assumes the legal risk; you just provide the data architecture.", "s": [0, 0, 0, 10, 0]},
                {"t": "Flat out refuse to build it, citing the Works Council agreement and the catastrophic impact on psychological safety.", "s": [10, 0, 0, 0, 10]},
                {"t": "Build a dummy version of the dashboard with aggregated, non-individualized data to placate the COO while avoiding direct violations.", "s": [0, 0, 0, 5, 5]},
                {"t": "Present a thoroughly researched alternative: a dashboard focusing on team-level output and project velocity, persuading the COO that surveillance hurts results.", "s": [10, 10, 5, 5, 10]}
            ]
        }
    ]