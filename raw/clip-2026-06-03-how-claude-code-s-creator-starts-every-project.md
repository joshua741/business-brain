---
name: clip-how-claude-code-s-creator-starts-every-project
type: source
tags: [video, transcript]
status: complete
sources: [clip-2026-06-03-how-claude-code-s-creator-starts-every-project.md]
updated: 2026-06-03
---

# How Claude Code�s Creator Starts EVERY Project
**Source:** https://www.youtube.com/watch?v=KWrsLqnB6vA   **Duration:** 00:12:16

## Summary
This video delves into the advanced workflow strategies of Boris Cherny, the creator of Claude Code, to maximize productivity and achieve better results with AI. The speaker emphasizes that while Boris has an engineering background, the principles he employs are universally applicable. The core thrust of the video is to move beyond simply typing requests into an AI and instead adopt a more structured, thoughtful approach that leverages planning, continuous improvement, verification, parallel processing, and automation.

The report breaks down Boris's system into six key strategies: utilizing "Plan Mode" for thorough upfront planning, maintaining a concise and effective "Claude.md" instruction file, implementing "Verification" loops to ensure AI output quality, "Multiplying Yourself" through parallel AI sessions, systematizing "Inner Loops" with Claude Skills, and adopting a "Build for the Future" mindset that anticipates continuous AI model improvement. By focusing on these principles, users can avoid common pitfalls like vague requests and bloated instruction sets, ultimately leading to more accurate, efficient, and scalable AI-assisted workflows.

## Key Takeaways
-   **Plan Mode is crucial:** Start 80% of AI sessions in a planning phase to clearly define the problem and desired outcome before building.
-   **AI solves problems quickly, not always correctly:** Vague requests lead to wrong solutions and debugging. Proactive planning helps align AI's understanding with your actual needs.
-   **"Move slow to move fast":** Thorough upfront thinking makes execution almost automatic and more accurate.
-   **Keep Claude.md minimal:** Avoid bloating your instruction file. Delete and start fresh if it becomes too long, as models improve over time.
-   **Implement verification loops:** Give Claude a way to check its own work, which can significantly improve output quality.
-   **Multiply yourself with parallel sessions:** Run multiple, partitioned Claude sessions simultaneously for different tasks to avoid context overlap and improve problem-solving.
-   **Systematize "inner loops" with Claude Skills:** Automate repetitive tasks by documenting processes as skills, making them infinitely repeatable and efficient.
-   **"Never bet against the model":** AI models are constantly improving. Focus on building robust systems and feeding quality information (your "Information Moat") rather than endlessly optimizing prompts that will soon be obsolete.

## Frameworks / SOPs
-   **Plan Mode:** This is a preliminary phase where the user engages with Claude Code to thoroughly define a project or problem before any building or coding begins. The goal is to ensure Claude understands the core problem, target audience, success metrics, and what the solution should *not* do. This involves an "interview" process where Claude proactively asks clarifying questions, helping to identify and fill gaps in assumptions. The principle is "move slow to move fast," ensuring the AI is on the right track from the start, making the execution phase more automatic and accurate.
-   **Claude.md:** This is a specific file that Claude Code reads every time a new chat session begins. It acts as a personalized instruction set or "cheat sheet" for Claude, guiding its behavior and preferences. The SOP for Claude.md involves keeping it minimal and updating it only when a mistake occurs, to prevent recurrence. If the file becomes too bloated, the recommendation is to delete it and start fresh, as AI models continuously improve and may no longer need overly specific or outdated instructions.
-   **Verification Loops:** This is a process to ensure the quality and correctness of Claude's output. It involves giving Claude a "tool" to observe the results of its work (e.g., server output, web UI, test results) and then instructing Claude on how to interpret and use that tool for self-correction. For creative tasks, it involves prompting Claude to review its output against specific guidelines. A general SOP is to add a line to `Claude.md` stating: "Before you do any work, mention how you could verify that work."
-   **Multiply Yourself (Parallel Sessions):** This strategy involves running multiple, independent Claude Code sessions simultaneously, each focused on a distinct, partitioned task. The core idea is that "two context windows that don't know about each other tend to have better results." By isolating tasks, each session can approach its problem with a "fresh context" or "no baggage," potentially identifying solutions that a single, deeply entrenched session might overlook due to accumulated context.
-   **Your Inner Loop (Claude Skills):** "Inner loops" refer to repetitive tasks performed frequently throughout the day. Claude Skills are a way to document these processes so they can be called directly within Claude Code to be completed consistently every time. This systematizes workflows, transforming complex, multi-step actions into single, repeatable commands. An example given is a skill to generate a specific report, ensuring consistent format and style with only the input data changing.
-   **Build for the Future (Information Moat):** This is a mindset shift emphasizing that AI models are constantly improving. Instead of spending excessive time on "optimized prompts" that might become irrelevant quickly, the focus should be on building an "Information Moat." This refers to the quality and structure of the information fed to the model and the overall system used to interact with AI, which will yield better results over time regardless of model updates. The principle is "never bet against the model" and plan for its continuous advancement.

## Timestamped Transcript
[00:00] Boris Cherny, the creator of Claude Code, says that his setup is pretty vanilla. So I started researching Boris and how he works. I dug up interviews, threads, everything he's shared publicly about how he actually uses Claude Code.
[00:12] Despite him having an engineering background, all the principles he uses, anyone can apply. So in this video, I'm going to show you exactly how he starts every project and show you how I've personally been applying these workflows.
[00:22] Let's get into the first section, which is all about Plan Mode. So here's one of the biggest features that you're probably missing. And here's a clip of him talking about how he uses it and how he babysits Claude Code.
[00:31] Probably 80% of my sessions I start in plan mode. And once the plan is good, it just stays on track. And it'll just do the thing exactly right almost every time. And so, you know, before you had to babysit after the plan and before the plan. Now it's just before the plan.
[00:45] So 80% of his sessions start in Plan Mode. And he clearly outlines the importance of babysitting before Claude Code starts building. And he mentioned that once a good plan is locked in, building is almost automatic.
[00:55] So why does this matter so much? Well, most people, they open Claude Code, they type what they want, and then they let it run. And there's really not a lot of planning that's involved. And yes, AI is great at solving problems, but the problem it thinks it should be solving and the problem that you actually want it to solve aren't necessarily the same thing.
[01:12] If your request is vague, you get the wrong solution. And then you spend hours debugging something that you could have avoided from the start. And generally speaking, AI is set up to solve problems as quickly as possible, not necessarily correctly.
[01:24] So you may think a problem is solved, but it didn't actually solve what you wanted it to solve. And I've seen this firsthand. So one of the clients I was working with, they had a bug on their website and the numbers weren't correctly displaying.
[01:36] And instead of fixing the display, Claude actually went into the database where it was getting the information, changed the value, and then marked it as resolved. It fixed one thing, but then that broke like five other things in the app because it changed the value.
[01:48] So it didn't actually solve the problem the way we wanted to solve it. And so Boris's approach is different, right? He's not trying to just attack it right away, he's planning.
[01:56] There's a quote that I love to reference from the Navy Seals, and it's "move slow to move fast." He has all the thinking that happens upfront, and then the execution is essentially automatic.
[02:05] So before you build anything, hit Shift+Tab twice in your terminal, and that will enter Plan Mode in Claude Code. So go back and forth until it's something you really like. Perhaps ask it to interview you to see if there's any gaps in your assumptions.
[02:17] And then you can have it start building. Here's a specific prompt you can use: "Before we start building, interview me about this: What is the core problem this solves? Who is this for? What does success look like? What should this NOT do? Summarize it back to me before we write any code."
[02:30] Now Claude will proactively ask you questions about things that it previously probably would have made assumptions about. So this was all about putting Claude in the best position to succeed. Now the next part is probably what surprised me the most about his entire strategy.
[02:44] Section 2: Claude.md. So, when you've used Claude Code, you might have seen a file called Claude.md. It's essentially a set of instructions that Claude reads every time you start a new chat.
[02:54] Think of it like giving Claude a cheat sheet about how you want to work, and it's specific to you. And Boris uses this how a lot of people use it. Whenever there is a mistake, he'll update the Claude.md file to make sure it doesn't happen again.
[03:06] A simple prompt that you could use here is: "Based on this conversation, can you update Claude.md so this doesn't happen again." And this is extremely powerful, but there are limitations.
[03:15] And a lot of people, they think the more instructions that I give, I'll get better results. So they just create this massive Claude.md file with like every rule they can think of, and they never try and clean that up. But Boris does the opposite.
[03:27] Here's a clip of him talking about how he handles it when this file is getting extremely long.
[03:32] So our Claude.md is actually pretty short. I think it's like a couple thousand tokens, something like that. Um, if you, if you hit this, my recommendation would be delete your Claude.md and just start fresh. Interesting. I think a lot of people like they try to over-engineer this, right? And and really like the capability changes with every model. And so the thing that you want is do the minimal possible thing in order to get the model on track. And so if you delete your Claude.md and then, you know, the model is getting off track, it does the wrong thing, that's when you kind of add back a little bit at a time. And you, we are probably going to find as with every model, you have to add less and less.
[04:03] His advice is counter-intuitive, at least to me. But what he's saying is that if Claude.md is bloated, just delete the entire thing and start fresh. And his point is that because these models are getting better every day, what you needed six months ago is likely built into the model right now.
[04:16] And generally, if you give it a ton of instructions, the more you give it, the more likely Claude is going to get confused and not apply the rules that are actually critical. So he'll just delete the whole thing, which for me is a little bit scary, and that might be him just believing in Claude a little bit too much.
[04:33] Honestly, I'm not sure about that, but Boris's approach where he says, "do the minimal possible thing to get the model on track," is absolutely spot on. And what he does is, if he sees the same issue again, he'll just add it to the Claude.md.
[04:45] To be totally honest, this isn't something that I do. I feel like I'm a little scared. But what I do do is instead of deleting it, I run a simple command. I say, "Update my Claude.md to remove anything that's no longer needed, contradictory, duplicate information, or unnecessary bloat impacting effectiveness."
[05:02] I've found that this is an effective middle ground, but feel free to take Boris's advice and just periodically YOLO and delete the entire thing. And if you're not using the Claude.md file and updating it over time, make sure to do that.
[05:14] So now these first two strategies that we've covered are all about getting better results. But how do you actually make sure it did what you were hoping it was going to do?
[05:22] Section 3: Verification. The next key thing he does is about verification. Here's a post from Boris on Twitter that really stuck with me.
[05:29] "13/ A final tip: probably the most important thing to get great results out of Claude Code - give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result."
[05:35] In theory, this sounds awesome, right? You can just have Claude check what it did and see if it did it correctly. But how do you do this in practice? You can see his tweet on the screen, but he gives two steps.
[05:43] One, give Claude a tool to see the output of its work, and two, tell Claude about that tool. That's really it, and then he says Claude will figure out the rest. Again, Claude is pretty damn powerful.
[05:53] So for me and you, what does this look like in practice? If you're building something with a website, Boris uses Claude Code, opens a browser, tests what it built, and iterates until it actually works.
[06:02] And here are some other strategies if you're writing code. What's a bit more interesting for me are things that aren't necessarily right or wrong, like the more creative components.
[06:11] So if you're using Claude for content or writing, you could say, "Review this against my brand guidelines and flag anything that doesn't match." Or if you're building automations, you could say, "Run this workflow and verify the output matches what we expected."
[06:22] Above all that, the simplest approach that just kind of catches everything is you can add to your Claude.md: "Before you do any work, mention how you could verify that work."
[06:31] Now Claude will tell you what its verification plan is before it actually starts building. And if there's no clear way to verify it, maybe there's a better way to go about it.
[06:39] And a pro tip here, after going back and forth with Claude Code a bunch, here's something you could run. Say, "Please go back and verify all your work so far. Make sure you used best practices, were efficient, and didn't introduce any issues."
[06:50] So you're planning, you're keeping instructions minimal, and you're verifying. But what if you could do more at once? And this is probably the biggest force multiplier to increase your efficiency with these tools.
[06:59] This is about multiplying yourself. And Boris has a tweet where he talks about the importance of working in parallel. There's a lot of technical jargon here, like Git worktrees, and if you want to look that up on your own time, go ahead. But it probably doesn't matter because that's for more robust engineering teams.
[07:13] Instead of that, what's important for you is his concept of partitioning different workflows. He'll have multiple Claude sessions running at the same time, each one focused on a different task. And the key here is that each task is partitioned so they're not overlapping.
[07:28] A simple way to think about this is if you had two people working on the exact same thing at the exact same time, you'd have wasted effort, and they'd likely clash with whatever files you're working on. This is the same thing with Claude. If you have multiple sessions working on the same thing, it's counterproductive.
[07:42] Boris would approach it with this in mind. He says, "Two context windows that don't know about each other tend to have better results." So a fresh session could look at a problem with no baggage.
[07:52] And it might see something obvious that your first session missed because it was too deep in the weeds, and it had context that was fogging its problem-solving. Creating a new window and just starting from scratch is the equivalent of like, you turn it off and you come back and it just works.
[08:06] Now his fifth strategy is about creating an inner loop. Boris calls repeated tasks his inner loop. And these are things that he does many times throughout the day. You may not realize it, but if you think about it, you're going to find a lot of these inner loops.
[08:16] Quote from him: "I use slash commands for every 'inner loop' workflow that I end up doing many times a day. This saves me from repeated prompting and makes it so Claude can use these workflows." Slash commands allow me to do is just to quickly call things that he repeatedly does, and he's taken a more systematic approach.
[08:29] Now Boris uses something called slash commands to handle these more repeatable things that he does throughout the day, or his inner loops. But there's something called Claude Skills that's way more applicable to what you're doing.
[08:39] Claude Skills are essentially a way to document a process so that you can call it directly in Claude Code to complete that process every single time. In a sports analogy, let's say a prompt is you telling a player to like dribble the basketball, but a Claude Skill is the exact play to run. So that could be a pick and roll, and AI knows exactly how to run that play every single time.
[09:00] For Claude Skills, think about the inner loops that you have throughout the day. For me, some of these skills that I use for my clients, like one example, is I work with an engineering firm, and there's something called a Local Law 97 report, whatever, boring.
[09:11] But I'm able to use a skill, `/LL97-report-generator`, that generates the same report in the same format, in the same style every single time I run it, and the only thing that changes is the data that I reference.
[09:25] This is an inner loop that my team has to do throughout the day, but once we've created a skill for it, it's infinitely repeatable. These are so, so powerful, and I cannot stress how important these are. I have a full video on my YouTube where I break down exactly how I use Claude Skills and how you can use them.
[09:41] I'll reference it at the end of this video, but Boris uses this in his own way, and this is something that you just can't ignore. If you don't know where to start, just use this prompt: "Based on the project I'm working on, what Claude Skills should I create?" It'll give you the juice, you can just go from there.
[09:54] Now there's one more mindset shift that ties all of these different concepts together that Boris explains extremely well. The last section is "Build for the Future." This is something that a lot of people ignore. Here's an excerpt directly from Boris.
[10:05] We have a framed copy of "The Bitter Lesson" on the wall. Um, and this is this like Rich Sutton, uh, blog post that everyone should read it if if you haven't. Uh, and the idea is the more general model will always beat the more specific model. And there's a lot of corollaries to this, but essentially what it boils down to is never bet against the model.
[10:22] Restating this, every piece of scaffolding or micro-tweaks to improve the model's output that you do will probably be unnecessary in the next six months. And the reason is that the model's just getting better.
[10:33] Now, that's not a reason to not build things, but it's important to understand that AI models get better every single day. So, it's about thinking where should you focus your energy? And if you've watched some of my other videos, you know how stupid I think it is writing optimized prompts.
[10:48] Respectfully, to everyone out there who's saying to optimize prompts, because ultimately, the model is just getting better, and you don't really need an optimized prompt. You need to just give it the right direction.
[11:00] Instead, you should be spending your time on your "Information Moat," and that's everything that you're feeding the model and the system that you're using to get AI better over time. This is the context that is put on top of the model to get you those fire outputs.
[11:12] So, remember this when you're tweaking with prompts. Like, is this worth the 10% improvement right now, or should you just spend your time assuming the model will be better next month and working on other things?
[11:24] Because AI will never be as bad as it is today, which is frankly very scary. So with all that in mind, let's recap Boris's system.
[11:29] His first thing he does is he uses Plan Mode. Move slow to move fast. Have the conversation before Claude starts building. Two is create a minimal Claude.md file. Less is more, and if you have to, start fresh.
[11:41] Three is verification. Give Claude a way to check its own work. Four, multiply yourself. Parallel sessions, fresh context for hard problems. Five, systematize your inner loops. Document once, run forever, use Claude Skills.
[11:54] Six, build for the future. Expect that the models are going to get better, not worse. Plan accordingly.
[12:00] Now if you like this video, make sure to check out this video where I do a deep dive on Claude Skills and how you can transform your workflow and set up your own operating system. Combining the content I cover over there with the pro tips from Boris, you will become a Claude Code savage. I'll see you in the next one. Peace.

## Notable Quotes
-   "Probably 80% of my sessions I start in plan mode. And once the plan is good, it just stays on track." — [00:32]
-   "If your request is vague, you get the wrong solution." — [01:13]
-   "AI is set up to solve problems as quickly as possible, not necessarily correctly." — [01:20]
-   "Move slow to move fast." — [01:58]
-   "If you hit this, my recommendation would be delete your Claude.md and just start fresh." — [03:38]
-   "Do the minimal possible thing in order to get the model on track." — [03:50]
-   "If Claude has that feedback loop, it will 2-3x the quality of the final result." — [05:31]
-   "Two context windows that don't know about each other tend to have better results." — [07:44]
-   "I use slash commands for every 'inner loop' workflow that I end up doing many times a day. This saves me from repeated prompting and makes it so Claude can use these workflows." — [08:16]
-   "The more general model will always beat the more specific model." — [10:13]
-   "Never bet against the model." — [10:20]
-   "You don't really need an optimized prompt. You need to just give it the right direction." — [10:57]
-   "AI will never be as bad as it is today." — [11:24]

## On-screen Text & Visuals
-   **[00:00]** Text overlay: "BORIS CHERNY" and "CLAUDE CODE". Speaker in a "Creative" baseball cap.
-   **[00:02]** Screenshot of a tweet from Boris Cherny (@bcherny) dated Jan 3, 2026. Text highlighted: "My setup might be surprisingly vanilla".
-   **[00:07]** Various screenshots of Boris Cherny's interviews, Twitter threads, and a LinkedIn profile showing his experience at Anthropic as "Lead of Claude Code" and "Principal Software Engineer".
-   **[00:13]** Animated graphic: "Engineering Background" leading to "Principles he uses" which branches out to four generic person icons.
-   **[00:18]** Animated graphic: "How he starts every project" and "How I've been applying these workflows".
-   **[00:23]** Animated graphic: "Section 1 Plan Mode" with a pixelated red pig icon.
-   **[00:32]** Clip of Boris Cherny in an interview setting with four other people around a table.
-   **[01:05]** Animated graphic: "AI is Great at solving problems" connected to a pixelated red pig icon. Below, "The problem it thinks it should be solving" and "The problem that you actually want it to solve" are shown, with a "not equal" sign between them.
-   **[01:14]** Text overlay: "If your request is vague, you get the wrong solution".
-   **[01:16]** Speaker shown at his desk, typing on a laptop, with "reset" text overlay.
-   **[02:05]** Screen recording of a terminal window showing Claude Code. Text: "@plan-feature.md", "Skill (plan-feature)", "Successfully loaded skill", "Let's plan a feature together. I'll walk through this step by step.", "What's the Feature? Just describe what you want to happen - don't worry about how." Highlighted text: "accept edits on (shift+tab to cycle)" and "? for shortcuts hold Space to speak".
-   **[02:19]** Slide with "Prompt:" header and the text: "Before we start building, interview me about this: What is the core problem this solves? Who is this for? What does success look like? What should this NOT do? Summarize it back to me before we write any code."
-   **[02:44]** Animated graphic: "Section 2 Claude.md" with the pixelated red pig icon.
-   **[02:47]** Screen recording of a terminal window showing a file structure and content of "CLAUDE.md". Key sections visible: "# CLAUDE.md - PERSONAL OS", "## Folder Structure", "## Knowledge", "## Projects", "## How to Use Context", "## Key Principles", "## Project Lifecycle".
-   **[03:06]** Screen recording of a terminal window showing Claude Code interaction. User input: "Based on this conversation, can you update Claude.md so this doesn't happen again".
-   **[03:32]** Clip of Boris Cherny in an interview setting.
-   **[04:35]** Animated graphic with Boris Cherny. Text overlay: "Do the minimal possible thing to get the model on track".
-   **[04:54]** Screen recording of a terminal window showing Claude Code. User input: "Update my Claude.md to remove anything thats no longer needed, contradictory, duplicate information or unnecessary bloat impacting effectiveness".
-   **[05:22]** Animated graphic: "Section 3 Verification" with the pixelated red pig icon.
-   **[05:29]** Screenshot of a tweet from Boris Cherny (@bcherny) dated Jan 3. Text: "13/ A final tip: probably the most important thing to get great results out of Claude Code - give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result."
-   **[05:41]** Screenshot of a tweet from am.will (@LLMJUNKY) asking about quality validation loops, and Boris Cherny's reply: "1. Give Claude a tool to see the output of the code... 2. Tell Claude about the tool... That's literally it. Claude will figure out the rest."
-   **[05:56]** Screen recording of Claude Code interacting with a web page ("5 Mistakes Killing Your Claude Code Output"). Claude opens a browser, tests, and iterates.
-   **[06:03]** Slide with text: "If you're building server code - tell Claude to start the server and verify the endpoint responds correctly. If you're writing tests - tell Claude to run them and confirm they pass."
-   **[06:13]** Screen recording of Claude Code chat. User input: "Review this against my brand guidelines and flag anything that doesn't match".
-   **[06:17]** Screen recording of Claude Code terminal. User input: "Run this workflow and verify the output matches what we expected".
-   **[06:28]** Slide with text: "Add this line to your Claude.md: Before you do any work, mention how you could verify that work."
-   **[06:43]** Slide with "Prompt:" header and the text: "Please go back and verify all your work so far. Make sure you used best practices, were efficient, and didn't introduce any issues."
-   **[06:59]** Animated graphic: "Section 4 Multiply Yourself" with the pixelated red pig icon.
-   **[07:00]** Screenshot of a tweet from Boris Cherny (@bcherny). Text: "1. Do more in parallel! Spin up 3-5 git worktrees at once, each running its own Claude session in parallel. It's the single biggest productivity unlock..."
-   **[07:18]** Screen recording of a terminal window showing multiple Claude Code sessions running in parallel, each with a different "worktree" name.
-   **[07:43]** Animated graphic with Boris Cherny. Text overlay: "Two context windows that don't know about each other tend to have better results".
-   **[08:07]** Animated graphic: "Section 5 Your Inner Loop" with the pixelated red pig icon.
-   **[08:16]** Screenshot of a tweet from Boris Cherny (@bcherny). Text: "7/ I use slash commands for every 'inner loop' workflow that I end up doing many times a day. This saves me from repeated prompting..." Example: "/commit-push-pr Commit, push, and open a PR".
-   **[08:39]** Slide with text: "Claude Skills: a way to document a process so that you can call it directly in Claude Code to complete that process every single time."
-   **[09:12]** Screen recording of a terminal window showing a Claude Skill definition: "/LL97-report-generator skill generates client-ready NYC Local Law 97 Carbon Emissions Reports for [redacted] CEM." Details on "What it does" and "Usage".
-   **[09:35]** YouTube video thumbnail: "19 Things You Didn't Know Claude Skills could do" by Austin Marchese.
-   **[09:47]** Slide with "Prompt:" header and the text: "Based on the project I'm working on, what Claude Skills should I create?"
-   **[09:59]** Animated graphic: "Section 6 Build for the Future" with the pixelated red pig icon.
-   **[10:05]** Clip of Boris Cherny in an interview setting.
-   **[10:56]** Text overlay: "You don't really need an optimized prompt. You need to just give it the right direction."
-   **[11:02]** Text overlay: "Information Moat: everything that you're feeding the model and the system that you're using to get AI better over time."
-   **[11:29]** Slide: "BORIS'S SYSTEM RECAP" with a numbered bullet list:
    1.  Plan mode: Move slow to move fast. Have the conversation before Claude starts building.
    2.  Claude.md: Create a minimal Claude.md file. Less is more, and if you have to, start fresh.
    3.  Verification: Give Claude a way to check its own work.
    4.  Multiply Yourself: Parallel sessions, fresh context for hard problems.
    5.  Your Inner Loop: Systematize your inner loops. Document once, run forever, use Claude Skills.
    6.  Build for the Future: Expect that the models are going to get better, not worse. Plan accordingly.
-   **[12:01]** End screen with a link to another YouTube video by Austin Marchese.

## Action Items
-   Start 80% of your AI sessions in "Plan Mode" by hitting Shift+Tab twice in the Claude Code terminal.
-   Use the interview prompt in Plan Mode: "Before we start building, interview me about this: What is the core problem this solves? Who is this for? What does success look like? What should this NOT do? Summarize it back to me before we write any code."
-   Maintain a minimal `Claude.md` file, updating it only when mistakes occur to prevent repetition.
-   If your `Claude.md` becomes bloated, either delete it and start fresh (Boris's advice) or use the prompt: "Update my Claude.md to remove anything that's no longer needed, contradictory, duplicate information or unnecessary bloat impacting effectiveness."
-   Implement verification loops for Claude's work by giving it tools to see its output and instructing it on how to use them.
-   For creative tasks, prompt Claude to "Review this against my brand guidelines and flag anything that doesn't match."
-   For automations, prompt Claude to "Run this workflow and verify the output matches what we expected."
-   Add the line "Before you do any work, mention how you could verify that work" to your `Claude.md` file.
-   Periodically run the prompt: "Please go back and verify all your work so far. Make sure you used best practices, were efficient, and didn't introduce any issues."
-   Partition your AI workflows by running multiple, independent Claude sessions for different tasks.
-   Identify your "inner loops" (repetitive daily tasks) and create Claude Skills to automate them.
-   If you don't know where to start with Claude Skills, use the prompt: "Based on the project I'm working on, what Claude Skills should I create?"
-   Focus on building your "Information Moat" – the quality of data and systems you feed the AI – rather than constantly optimizing prompts.
