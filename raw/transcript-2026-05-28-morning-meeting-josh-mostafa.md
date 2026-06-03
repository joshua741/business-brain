# Morning Meeting Josh, Mostafa 2026-05-28T12:00:00.000-05:00

*(Pulled from Notion by the notion-meetings connector on 2026-06-03.)*

---

### Action Items

- [ ] Joshua to follow up with Joseph about new monthly payment options at 4019 37th Street  

- [ ] Send Joseph voicemail explaining insurance bundling requirement and payment scenarios ($1,813 if escrowed vs $1,840 if month-to-month)   

- [ ] Tracy to cash check before making escrow shortage payment for 2802 South Channing  

- [ ] Send Tracy invoice for $1,172.98 escrow shortage payment once check is cashed  

- [ ] Obtain tax reduction documentation from city for 2802 South Channing 

- [ ] Email tax reduction proof to Rocket Mortgage at oscorrespondence.ctax@corelogic.com with loan number, client name, and property address  

- [ ] Send amendment to contract to Michael Boulos and Kenneth for 4513 48th Street  

- [ ] Mustafa to complete door loop payment automation skill (currently 80-90% complete) 

- [ ] Complete property photo watermarking skill in Claude for Canva integration  

- [ ] Reach out to Esther Cantu (ongoing attempts, calls going to voicemail)  

### LLM Wiki Technical Training

Joshua and Mustafa spent time learning about LLM Wiki systems through educational videos.   The discussion focused on understanding how to use Claude Code with Obsidian to build persistent knowledge bases that organize information into interconnected markdown files.  

Mustafa expressed confusion about the practical applications, questioning what the tool is for and how it would be useful for their business.    Joshua explained the concept as a way to maintain organized information so they don't have to restart explanations each time, and to keep a knowledge base that continues to grow.  

The training covered the three-layer system: raw sources (documents/transcripts), the wiki itself (markdown files created by AI), and the schema (rules document).    Setup involves using Obsidian as a viewer and Claude Code for processing, with the ability to ingest various document types and automatically organize them with relationships and backlinks.   

Joshua asked Claude AI to research and explain LLM Wiki in simple terms based on the videos watched.   

### Property: 4019 37th Street (Joseph's Property)

Received insurance quote from Allstate requiring bundling of car and home insurance.   Car insurance liability quote came in at $151.13 per month.  

Home insurance has two payment structure options:  

- $328 per month if mortgage company escrows the payment (pays annually upfront)  

- $355 per month if structured as month-to-month payment 

Total monthly payment scenarios:  

- $1,813 if bank approves escrow

- $1,840 if month-to-month payment required

The difference is $27 per month between the two options.  Current payment breakdown includes principal and interest ($1,203.35), taxes ($281.15), and insurance ($328 or $355).   

Joshua left detailed voicemail for Joseph explaining all options and noting they will credit two payments already received to the servicing company.   

### Property: 2802 South Channing (Tracy's Property)

Called Rocket Mortgage to determine escrow shortage amount: $1,172.98 remaining.   Tracy needs to cash her check before this payment can be processed.  

Discussed strategy to reduce Tracy's monthly payment, which is currently $2,103.83.  The payment is broken into five components:  

- Principal and interest (fixed, never changes) 

- Taxes (can be reduced with new assessment)  

- Insurance (minimal $27 potential reduction) 

- Private Mortgage Insurance ($116.42/month)  

- Escrow shortage (temporary increase)  

PMI removal requirements confirmed with Rocket Mortgage: Cannot be removed until loan term ends because this is an FHA loan with less than 10% down payment.    Standard PMI removal typically requires 20% equity and 12 consecutive on-time payments, but rules vary by lender.   

Tax reduction strategy: Property taxes have been reduced by the city after claiming homestead exemption.   Need to send proof of tax reduction to oscorrespondence.ctax@corelogic.com to trigger early escrow analysis.   This will reduce both the shortage amount and ongoing monthly tax payments.  

Contact information obtained: Tax reduction documentation should include client name, loan number (110-825-7000.263.7491), and property address.  

Discussed potential insurance bundling option with Allstate to further reduce premiums.   

### Property: 4513 48th Street

Property photos received and reviewed.   Team discussed applying watermark to images before distribution.  

Need to send amendment to contract to Michael Boulos and Kenneth.   Kenneth already signed and received a copy, but will send to both for confirmation.  

### Workflow Automation Projects

Mustafa provided update on door loop payment automation skill - currently 80-90% complete but stuck at a manual setup step.  This skill will automatically check tenant payments in door loop and update spreadsheets. 

Joshua initiated creation of new property photo watermarking skill using Claude.   The skill will:   

- Take property images and overlay with company logo using Canva MCP integration

- Resize images to 940 x 626 pixels with logo at 410 x 248 pixels positioned in bottom right corner

- Organize photos in specific order: front exterior, living room, kitchen, master bedroom, master bathroom, secondary bedrooms, secondary bathrooms, additional rooms, back exterior  

- Save completed files with property address as filename

- Store brand assets in dedicated "Brand Themes" folder for future reference  

The skill will prompt for: file name, location, and desired placement of completed files (downloads, email, or custom location).  

### Personal/Administrative Notes

Mustafa explained he's currently working late hours (until 4-5 AM local time, around 8-9 PM Central) at family business property dealing with tenant dispute.   Former tenant with 7-9 year lease is not maintaining garden areas they agreed not to use in exchange for not increasing rent to market rate.   Mustafa staying on-site to ensure tenant doesn't return to those areas. 

Joshua ended meeting early, realizing scheduled call with Sharon was at 2:30 PM, not 3:30 PM. 

Hey, Josh.

Mr. Mustafa, what's going on brother? youDoing well, man.

I'll do it, I'll do it. How's it going, sir?

Just over here about to watch a quick video with you.

Pretty much get right into it, man. Anything that you wanted to touch on?

Touch on before we get started.

I mean, I've been, Being a very geeky nerd since yesterday using Cloud code vs studio and all this stuff Even cloud code got stuck at a part and asked me to to do a manual What can I say?

Mm hmm.

Manual setup.

It was way too technical, so I jumped into it.

Excellent, excellent.

I faced a couple of...

What I want to go over today is skills. There is a skill that there is obviously, now you won't be doing this part right now until I know that I feel safe around it, but I do want to demonstrate.

But yeah, I mean, once we finish this part here, we can get into it and show you exactly where I am.

Download a few skills.

If you want to watch a quick video on doing so, at least the most popular skills that they are.

you you Okay.

Let's do it. I mean, I do the same, so don't worry.

So as agent decoding is improving, one of the main things that we're doing to get these improvements is by including a bunch of markdown files and skill files to teach these models and these harnesses how to actually write the code and kind of follow along the path that's needed.

I want to download those, but I want to figure out what they do. But the two skills that I want to download, one is a brainstorming skill. Another one is a research skill. We'll look online for research. That would definitely help me out, especially when it comes to some of these things that we're doing. But again, my biggest thing is that I don't just add skills for no reason. I want them to actually be relevant to what I know that we're doing.

You get what I'm saying?

So that's where it's really important. So let's go ahead and share this video. You're probably going to see me kind of jumping around a little bit, but it's because I just want to get to the point.

A little bit soThere we go. And one thing too, I watch videos on like, half speed so that I don't have to... It saves time.

What you're looking at right here is 36 of my most recent YouTube videos organized into an actual knowledge system that makes sense.

Sometimes I do.

OK, so something I want to figure out real fast.

What does the McCarthy skill do?

I'm going to show you how you can set this up in five minutes.

Hmm.

It's super, super easy. You can see here how we have these different nodes and different patterns emerging. And as we zoom in, we can see what each of these little dots represents. So for example, this is one of my videos, $10,000 genetic workflows. We can see it's got some tags. It's got the video link. It's got the raw file. And it gives an explanation of what this video is about and what the takeaways are. And the coolest part is I can follow the backlinks to get where I want. There's a backlink for the WIT framework.

There's a backlink for cloud code. There's a backlink for all these different tools I mentioned, like perplexity, visual studio code, nano banana, and it also has techniques like the WIT framework or bypass permissions mode.

human review checkpoint. So as this continues to fill up, we can start to see patterns and relationships between every tool or every skill or every MCP server that I might've talked about in a YouTube video. And I can just query it in a really efficient way now that we have this actual system set up. And the crazy part is I said, Hey, cloud code, go grab the transcripts from my recent videos and organize everything. I literally didn't have to do any manual relationship building here.

It just figured it all out on its own. And then right here, I have a much smaller one, but this is more of my personal brain. So this is stuff going on in my personal life. This is stuff going on with, you know, up AI or my YouTube channel or my different businesses and my employees and our quarter two initiatives and things like that. This is more of my own second brain. So I've got one second brain here.

And then I've got one basically YouTube knowledge And I could combine these or I could keep them separate and I can just keep building more knowledge systems and plug them all into other AI agents that I need to have this context. It's just super cool. So Andre Karpathy just released this little post about LLM knowledge bases and explaining what he's been doing with them. And in just a matter of a few days, it got a ton of traction on X. So let's do a quick breakdown and then I'm gonna show you guys how you can get this set up in basically five minutes. It's way more simple than you may think. Something I've been finding very useful recently is using LLMs to build personal knowledge bases for various topics of research interest. So there's different stages. The first part is data ingest.

He puts in basically source documents. So he basically takes a PDF and puts it into Cloud Code and then Cloud Code does the rest. He uses Obsidian as the IDE. So this is nothing really too game-changing.

your markdown files. But for example, this Obsidian project right here with all this YouTube transcript stuff, that actually lives right here. This is the exact same thing. Here are the raw YouTube transcripts. And here's that wiki that I showed you guys with the different folders for what Cloud Code did with my YouTube transcripts. And then there's a Q&A phase where you basically can ask questions about YouTube or about the research, and it can look through the entire wiki in a much more efficient way.

And it can give you answers that are super intelligent. And you're because it finally makes a deal because normal AI chats are ephemeral, meaning the knowledge disappears in that node or in that relationship. And it can go to research and fill in the gaps. All right, so why is this a big deal? Because normal AI chats are ephemeral, meaning the knowledge disappears after the conversation. But this method using Thank you.

After that, I have all the different techniques, agent teams, sub-agents, permission modes, the WAT framework. And then we've got different concepts, MCP servers, RAG, vibe coding. We've got all these different sources, which are the YouTube videos. And then when I have people or when I have comparisons, they will be put in here in the index. And then we also have a log, which is the operation history.

So in this case, in the YouTube project, the log isn't huge because I only ran one huge batch of the initial 36 YouTube videos. But now every time I have one, I say, hey, can you go ahead and ingest the new YouTube video into the wiki? And then we'll see every single time we update this. And then, of course, you need your Cloud.md to explain how the project works and how to search through things and how to update things. It's also a big deal from a cost perspective, token efficiency and long-term value.

user turned 383 scattered files and over 100 meeting transcripts into a compact wiki and drops token usage by 95% when querying with Claude. And obviously token management and efficiency is a huge conversation right now and will always be. The other thing that's really cool about this is there's not really like a GitHub repo you go copy or there's not a complicated setup. You literally just say, hey, Claude Code, read this idea from Andrej Karpathy and implement it.

And people on X are now talking about like, this is how 2026 AI agentic software and really just say, hey, Claude Code, read this idea from Andrej Karpathy and implement it. And people on X are now talking about like, this is how 2026 AI agentic software and products will be made. You just give it a high level idea and it goes and builds it out. And Karpathy even said, hey, you know, So that you guys can customize it and i'll show you the ways in my two different vaults right now that it changed things a little bit based on the context and understanding of what the project is actually for Okay, so this was the original tweet I just showed you guys and then he followed up and said hey this one went viral So here is the idea in a gist format So if you open this up This is basically just another explanation of the core idea of how this works and why the architecture indexing all this kind of stuff And by the way, this is the part where he says hey This is left vague so that you can hack it and customize it to your own project So we're going to come right back to this in a sec But the first prereq that we're going to do it's not necessary But I like to have a nice little front end to see the relationships is we're going to go to obsidian and download it So if you just go to obsidian.md, you can see this is the completely free tool and you're going to go ahead and So just for your operating system, download this and then open up the wizard and open up the app.

So when you open up the app, it'll look like this. And what we're going to do here is we're going to create a new vault. So down here, you can see I have HercBrain and I have YouTube transcripts. I'll just make it a little bigger. I'm going to go to manage vaults. I'm going to create a new one. And now we just have to give us a name. So I'm just going to call this one demo vault, and you're going to choose a location where you want to put this. So I'm just doing this on my desktop and I'm going to go ahead and create this vault.

Then what you're going to do is go to wherever you like to run cloud code. So in this case, I'm doing it in VS code and I open up that folder. So demo vault, we get an obsidian and then we get a welcome.md. So I'm going to open up cloud. So I'm going to do it in my terminal. I'm going to run cloud.

I like to do it inside of VS Code, but the reason is just because I like to see the status line and I have a little bit more functionality. So anyways, now that we have Cloud Code open, here's what we're going to do. We're going to go back over to the LLM Wiki thing that we got from Andre Carpathie. We're going to copy all of this.

and we're going to go back into Cloud Code and then just paste it in there. So that is the prompt from Carpathi that's going to build out everything we need. And then before we send that off, we're dropping this in, which you guys can screenshot and then just throw into yours.

saying you are now my LLM wiki agent. Implement this exact idea file as my complete second brain. Guide me step by step, create the Cloud.md schema, blah, blah, blah. So this is just telling it what it needs to do with this idea that we just got from Carpathi. So anyways, on the right, we have this cloud code running. And on the left, we have our Obsidian vault. And you can see it just created those two folders.

So it created the raw and it created the wiki, as you can see. Now by default, it threw in four folders. It threw in analysis, concepts, entities, and sources. Once we start to populate stuff, we can talk to it to see if that's actually the way we want to do it or not. Because it's interesting, in my personal kind of second brain, the wiki is literally just marked on files. There's no structure to it. And in some cases, that's good.

Carpathi actually said, sometimes I like to keep it really simple and really flat, not a bunch of over organizing. But then you guys did see in my YouTube transcript one, there were different subfolders. And I think that in this case, it actually makes more sense. But you can see that it went ahead and it created a cloud.md, it created an index and a log, and then a few different folders in our wiki.

But now it's saying, hey, let's go ahead and try it out.

Drop in your first source into the raw folder and tell me to ingest it. Okay, so I'm at this website called AI 2027. If you guys haven't read this before, it's kind of an interesting read, so go check it out. And now let's say I want to get this into my vault. What I could do is just copy the whole page, right? And it might just come through a little weird. Or we can just get an Obsidian extension, which lets us basically take articles right from the web and just put it right into our vault.

Super easy. So search for this extension called Obsidian Web Clipper. You would go ahead and add this to Chrome. So then when you're in the you want. You basically just click on your extensions, you open up Obsidian Web Clipper, and then you can just chuck it into your vault. And then right here, you're going to want to set this to raw because this is the actual folder that's going to put it in. So you can go ahead and click add to Obsidian, open Obsidian.

And then now you can see in my raw section, we have this AI 2027 source with the title, the source, and it's not super, super popular to get because the LLM and cloud code is going to do that. So here is our file. I'm going to open up cloud code and say, awesome. I just threw in an article called AI 2027 into the raw. Can you please go ahead and ingest that? It might ask you some questions. It might also be helpful to, before you start ingesting stuff, say, Hey, by the way, this project is specifically for my second brain.

So personal things, business things, whatever, or this is just a research where I'm going to chuck you all the articles and all the things that I want to learn about and all the things that I know. So there's different ways you can set up the project as you saw with mine, one for YouTube, one for just personal second brain. So now what it's doing is it's going to read through this article and then it's going to figure out where should I chuck everything into the wiki. It's not just going to create one MD file for this. It might create five or it might create 10 and there's going to be relationships between each of the different sections that it creates. So it's kind of doing its own method of chunking. Now, one thing I want to call out real quick is with this extension, if you go here and you open up the options for it, you can see that you can actually change where by default the folders are dropped, which is in the location section.

By default, it'll be going to a place called clippings, but just go ahead and change that to raw. Okay. So here it came back with all Right.

So what I'm thinking is that is almost like When we're doing like the research phase or whatnot, It's almost like we can be able to That's what I'm trying to figure out is like what is it for?

It said, here are my key takeaways from this article, blah, blah, blah.

And now it'll ask you, what do you want to emphasize from this article? What's your focus? How granular do you want to be? What's your plan? So I'm just going to say, I want this to be extremely thorough. This is my passion looking at where AI is going to go. And this whole project, by the way, that you're setting up in this vault is basically just going to be my place to dump in research about AI. So help me keep all that organized so that I can query it. And then I can, you know, keep my thoughts related. So that's just a quick example of what it might look like for you to give it some more context to continuously build your project. So I'm going to switch over over here to the graph view, because I think it'll be interesting to see as it is starting to go through and create those different wiki files.

It's going to go ahead and it's going to create all those relationships.

real time.

It seems like it's more like a general... way for it to be like for the for the project to be a lot more organized and central focused That's what it feels like, but I'm just trying to get that clear.

All right. So it's creating all of the wiki pages now. And you can see that it said it's going to make about 25 because there's so much stuff going on in the original AI 2027 article. Okay. So our first one just popped in here and there, a second one just came through. And now you can understand you're starting to see where do you have hubs or you just have little individual notes. So this is a major hub, someone named Eli, someone named Thomas, Daniel. And you can see all the different relationships here with things like AI governance, with things like open brain, superhuman coder. Okay.

So that ingest took about 10 minutes. So sometimes you have to be a little patient with, you know, reading through everything and organizing everything, but it does a lot of heavy lifting. Of course, when I uploaded the 36 YouTube transcripts in batch, it took about 14 minutes. So it kind of just depends, 23 wiki pages.

Just trying to get that clear. I see that, okay, cool, it's ingesting.

information on the internet.

We have a source. We have six people, five organizations, and one AI systems page, different concepts of technical alignment and geopolitical, and then an analysis. And then it asks some questions about it so that it can help make the relationships and make the structure even better. Now let's just open this one up a little bit deeper and see what it actually did in here with this stuff. So we have, this is the source with all the main relationships.

So as we start to add other articles, we will see.

See it.

See other big kind of like nodes and maybe in some cases we'll have relationships between like compute scaling with different articles that we upload as well So let's just see if I click into the main source we can see the tags that it got we can see the authors and we can Click around so here's a link to open AI.

transcribes it.

Basically,It's putting over there. I'm trying to figure out what's the relevance.

Okay, what's opening? I here's references in a I 27 here's some other connections with open AI like model spec. Okay, we're in model spec We can see other things about model spec and we can also go to how the LLM psychology model works. So this is just super, super cool.

Thank you.

All the relationships that we get.

And once again, all of this stuff that we're looking at was derived from one article and automatically organized and related. So the question now is like, what do we do from here? Do we query it inside of this environment? Do we query it from somewhere else? And that's completely up to the way that you want to use this. So for example, with my YouTube project, I'm probably just going to keep this here. And whenever I want to ask questions about YouTube, or if I want to turn this into like a website, I can just do that from here. Or if I need to, I can point a different project at this folder since everything's here and I can crawl through the wiki.

It can read the index and it knows how this stuff works because you can give it the Cloud.md so it understands the project as well.

Example in this one, which is just my second brain, where we have all the different things about like, I drop in my meeting recordings, I drop in, you know, ClickUp channels, summaries and things like that.

you That's a lot.

This is something that I want to use in my executive assistant. So what I did in my executive assistant here called Herc2, if I go to this cloud.md, you can see that we have a wiki path. So whenever you need to read things about me and my business that you don't have already, you would basically go to my Herc brain vault. You would go to that directory and then you would read through the wiki. You can read the hot cache, which I'll explain in just a sec. You can read the index, you can read the domain sub-index, and then you can also just search through everything here. And I said, don't read from the wiki unless you actually need it. So here are some things that you might do that you don't need to go read the wiki for.

And all of this is my business knowledge. Now, if you guys remember, I used to do this with context files inside of this project.

Okay, let me see if I can set this up real fast.

Okay, so there, Mustafa.

After this, we'll obviously get into it.

And when I changed over to this method, I actually saw a reduction in tokens that I was actually calling in this project. So the thing about the hot cache, right? I didn't actually have this in my YouTube one. So if I go to YouTube, you can see there's no hot cache. But if I go to the Herc brain in the wiki, you can see there's a hot.md right here. And this is basically just a cache. I used to do this with context files inside of this project. And when I changed over to this method, I actually saw a reduction in tokens that I was actually calling in this project.

So the thing about the hot cache, right? I didn't actually have this in my YouTube one. So if I go to YouTube, you can see there's no hot cache. But if I go to the Herc brain in the wiki, And this is basically just a cache of like 500 words or 500 characters that it saves, which is like, what is the most recent thing that Nate just gave me or that we talked about? In the context of my executive assistant, this is really helpful. You know, it might save me from having to crawl different wiki pages, but in something like the YouTube transcript project, I don't really need a hot cache.

So another thing that I alluded to, but didn't really cover was the idea of linting. So Prabhati says that he runs some LLM health checks over the wiki to find inconsistent data, impute missing data with web searches, find interesting connections for new article candidates, things like that. So it basically helps you run a lint, you know, every day, every week, whenever you want, which helps make sure that everything is scalable and structured in the right way.

And it might even come back and say, hey, Hopefully understand this. Can you give me some more info or can you grab some articles that might help me out? A sec, but the first prereq that we're going to do, it's not necessary, but I like to have a nice little front end to see the relationships, is we're going to go to Obsidian and download it.

So if you just go to obsidian.md.

Oh, yes, John, I'm sorry.

I didn't notice that. I was like, "Oh, I'm good." Yeah.

You can see this is the completely free tool in your vaults.

a new one and now we just have to give us a name. So I'm just going to call this one demo vault and you're going to choose a location where you want to put this. So I'm just doing this on my desktop and I'm going to go ahead and create a new vault. So down here you can see I have Herc brand and download it. So just for your operating system, download this and then open up the wizard and open up the app.

So when you open up the app, It'll look like this.

Okay, let's see.

This thing downloaded, almost downloaded.

And what we're going to do here is we're going to create a new vault. So down here, you can see I have HercBrain and I have YouTube transcripts. I'll just make it a little bigger. I'm going to go to manage vaults. I'm going to create a new one. And now we just have to give us a name. So I'm just going to call this one demo vault, and you're going to choose a location where you want to put this. So I'm just doing this on my desktop and I'm going to go ahead and create this vault.

Then what you're going to do is go to wherever you like this. And what we're going to do here is we're going to use the completely free tool and you're going to HercBrain and I have YouTube transcripts. I'll just make it a little bigger. I'm going to go to manage vaults. I'm going to create a new one. And now we just have to give us a name. So I'm just going to call this one demo vault and you're going to choose a location where you want to put this.

So I'm just doing this on my desktop and I'm going to go ahead and create this vault. Then what you're going to do is go to wherever you like to run Cloud Code. So in this case, I'm doing it in VS Code. And I open up that folder. So demo vault, we get an obsidian, and then we get a welcome.md. So I'm going to open up Cloud. So I'm going to do it in my terminal. I'm going to run Cloud. And lately, I've been liking to have YouTube transcripts.

I'll just make it a little bigger. I'm going to go to Manage Vaults. I'm going to create a new one. And now we just have to give this a name. So I'm just going to call this one Demo Vault. And you're going to choose a location where you want to put this. So I'm just doing this on my desktop. And I'm going to go ahead and create this vault. Then what you're going to do is go to wherever you like to run Cloud Code. So in this case, I'm doing it in VS Code.

And I open up that folder. So demo vault, we get an obsidian. And then we get a welcome.md.

There's a problem with the way most of us use AI right now. And once you see it, you're not going to be able to unsee it. When you upload documents to something like ChatGPT or Notebook LM and ask a question, the AI searches through your files, pulls out some relevant pieces, and gives you an answer. That works, but here's the thing. Ask a similar question tomorrow, and the AI does all of that work again from scratch.

Nothing was saved. Nothing was built up. Every single question starts from zero. Andrei Kapathy, one of the biggest names in AI, co-founder of OpenAI, former AI director at Tesla, recently shared an idea that fixes this problem. He calls it the LLM Wiki. Honestly, once you understand what it does, the old way of working with documents starts to feel broken. In this video, I'm going to walk you through exactly what the LLM wiki is, why it matters, and then we're going to build one together from scratch, step by step. You don't need to be technical. If you can create a folder on your computer, you can do this.

Hi, I'm Jamie, and welcome to Feature Stack. So let me explain the problem a bit more clearly, because this is important. The way most AI tools handle your documents right now is called RAG, Retrieval Augmented Generation. You upload some files, you ask a question, the AI searches through those files, grabs the chunks that seem relevant, and generates an answer. And that's fine for simple questions.

But what if your questions require connecting ideas across five different documents? The AI has to find all those pieces and stitch them together every single time. There's no memory, there's no accumulation, nothing compounds. Think about it like this. Imagine you're a researcher and you've been reading papers on a topic for weeks. With RAG, every time you ask the AI a question, it's like it's never read any of those papers before.

It starts fresh every time. That's the bottleneck. Garpati's idea flips this completely. Instead of searching raw documents every time you ask a question, Read your documents once and build a structured wiki out of them. A real persistent knowledge base made of interlinked markdown files. So when you add a new source, say a PDF or an article, the AI doesn't just store it for later. It actually reads it, extracts the key ideas, and integrates them into the wiki. It updates existing pages.

It creates new pages for new concepts. It links related ideas together. And if the new sources contradict something already in the wiki, it flags that too. So over time, the wiki keeps growing and getting richer. The connections are already there. The synthesis is already done. When you ask a question, the AI is not starting from scratch. It's actually working from a pre-built, organized knowledge base.

Here's how Kikofi describes it. He says, think of Obsidian as the IDE, the LLM as the programmer, and the wiki as the code base. You rarely write the wiki yourself. The AI does the writing and organizing. You focus on what goes in and what questions ask. The whole system has three layers and they're very simple.

What's the transcriptions?

PDF articles, blog posts, meeting notes, transcripts.

Layer one, your raw sources. These are your original documents like PDFs, articles, meeting notes, whatever you're working with. The important thing is that these are read-only. The AI reads them but never changes them. This is your source of truth. Layer two is the wiki itself. This is a folder of markdown files that the AI creates and maintains. It's whatever you're working with.

We literally are doing transcriptions right now.

The important thing is that Thank you.

Image, data files, this is your source of truth. Okay, so... Wow, okay, so it just Okay, so right now it seems like if it gets, this is basically like the brain of it.

Tell the AI how to structure the wiki, how to handle new sources, how to format everything. If you're using Cloud Code, this would be your cloud.md file. If you follow my other Cloud Code series, you already know what that is. If you're new to Cloud Code, I'll put the link to my beginner's video right up there. All right, let's get into the setup. Here's what we're going to need. First, Obsidian. This is a free note-taking app that works with plain Markdown files. It's going to be our viewer. You can download it at obsidian.md.

I'll put the link down below in the description. And don't worry if you've never used Obsidian before. I'll walk you through the parts that matter. Second, an AI coding engine. I'm going to be using Cloud Code for this because this is what I've been using in my series, and it works really well for this. But you could also use OpenAI Codex, Cursor, or other tools that can read and write files on your computer.

Now, I just want to point out, I'm using Obsidian because it has the graph view that makes the connections really visual. But this is just a folder of Markdown files. You could use VS Code or text editor, whatever you're most comfortable with. Once you've got Obsidian installed, just go ahead and open it. And the first thing what I'm going to do is just go and create a new vault you'll see right here. And this is just a fancy name for a folder.

So I'm going to go create, and I'm going to call this one LLM Wiki. And I'm just going to save it some more simple. I'm just going to put it into my documents here. You'll see there. And you can put it where you'd like. I'm going to go and hit create. Now we need to set up a folder structure. I'm going to create three folders. The first one's going to be raw. I'm just clicking right up here, new folder, and I'm going to call it raw.

The AI will read from this, but never change anything in here. The second folder is going to be Wiki. This is where the AI will build and maintain all of its pages. And the third folder is going to be called templates. This templates folder is optional. If you wanted to manually create notes in Obsidian with consistent format, you could put a template right But since Claude is going to be creating all of our wiki pages for us, we don't.

Okay.

So, hello, film, wiki.

The AI will open it. And the first thing I'm going to do is just go and create a new vault you'll see right here. And this is just a fancy name for a folder. So I'm going to go Create. And I'm going to call this one LLM Wiki. And I'm going to save it somewhere simple. I'm just going to put it into my documents here. You'll see there. And you can put it where you like. I'm going to go and hit Create. Now we need to set up a folder structure. I'm going to create three folders.

The first one's going to be raw. I'm just clicking right up here, New Folder. And I'm going to call it raw. The AI will read from this but never change anything in here. The second folder is going to be wiki. This is where the AI will build and maintain all of its pages. And the third folder is going to be called templates. This templates folder is optional. If you wanted to manually create notes in Obsidian with consistent format, But since Claude is going to be creating all of our wiki pages for us, we don't need it for this tutorial.

Create.

It's just here as a point to tell you about.

Browse folder.

Okay. First one. was going to be raw. Want to blow that one?

So here's what a structure looks like.

We have our wiki, templates, and raw. Nothing too complicated with this. We need to create the schema file, the rules document that tells the AI how to operate the wiki. If you're using Cloud Code, you're going to create a file called cloud.md in the root of your vault. So this is the file that Cloud Code reads automatically when it opens a project. So I'm going to give you a starter template that you can copy.

It's linked down below in the description. But let me walk you through what's in it. Now, first of all, I'm just going to bring the cloud.md file into the root right here. So I'm just going to drop it so we can have it here. You can see my other folders are here. But here's the cloud.md file. So if I click on it, you're going to be able to see what's in it. Now, first, the purpose right here. So this is the purpose of the wiki.

What's the knowledge base about? So in our template, I've set this to planning a trip to Japan because this is what we're going to do in the demo today. But when you download this file, this is the one line you can change to match whatever you're going to be building a wiki about. If you're wanting to track books that you want to learn from, change it to that. Everything else in the template works as is.

The purpose of the line is the only thing that you really need to customize to get started. Second, the folder structure. Where are the raw resources? Where's the wiki output? What goes where? Third, the ingest workflow. When you add a new source document, what should the AI do? The basic steps are read the document, extract key concepts, create the update wiki pages, update the index, and log what changed.

Fourth, page formatting rules. Things like every page should have a summary at the top. Every claim should reference its source. Pages should link to related concepts. And fifth, the question answering behavior. When you ask the AI a question, it should consult the wiki first, cite its sources, and tell you when something is uncertain. Now, don't overthink this. The template I'm giving you gives you a solid starting point. Find it as you go.

That's actually part of the process. The schema evolves as the wiki grows. I'm also going to add this Obsidian extension here as a web clipper. So I'm going to go ahead and add this to Chrome. It's free to do. And what I'm going to do is convert any web articles into a markup.

Obsidian Web Clipper.

Okay, all right.

Interesting. I'll go ahead and I'll I'll get this and... I think I'll just do some. More. Research on the side.

So this tool here, Josh, what is it similar to?

Nothing that I know of.

Thank you.

Okay, nothing I know of.

Hey. Okay. I'm just a little bit confused. What does it do exactly? Is it an AI component?

Is it way four?

I mean, isn't it what.

AI to basically keep and maintain and organize the big picture. So that's what I'm getting for right now.

He'll does.

I don't know. I don't know everything. So that's what it feels like thus far is that what it is, is that it's going ahead and Just... ingesting a lot of information. I don't know yet what this is for. I don't know yet. But it seems like it will keep it more on track. I just need to watch a few more videos to kind of understand what it is. what is doing. But anything that can keep me more organized where I don't have to That is one big thing that is like, That will save me a ton of time is where I don't have to restart every single time of re-explaining why this is important.

What we're looking to do, what we've done in the past and stuff like that. If it already has that in like conceptually, that would be huge. So that's something that I wanted to add on top of wanting a researcher. As well as... wanting something so that when we add files and stuff like that. Like we're talking about getting new skills and things such as this. it filters it to make sure that it is safe to use.

down file so it's super handy all right now here comes the fun part let's feed the wiki with its first document now i'm Hello?

Okay, I'm back.

No, you're good. You know what? I have an idea. Maybe this can help us out.

I don't know what happened. I am back.

Um, Why do this? This should help us out. Because we don't really understand what it is.

So we heard this thing called LLM Wiki. And it seems like it's a way that Claude can be able to Keep a knowledge base. that continues to grow in short. I am just having a bit of a heart issue conceptualizing.

where I can use this.

and why it's important. Could you do some research off of these videos that explains What is for? As well as do your own research as well and explain it back to me as if I'm a fifth grader that does use Claude Code. It has general information that's pretty high level because of the fact that we're implementing it. but can still break this down in a way that simple so that we can be able to generally understand what's going on.

So I'm gonna give you two videos to watch as well as do some quick research and let us know what this is and how we can use it.

There's a lot of people There's a problem with the way Give me one second, Josh.

Okay. So then... What I do is I add this skill on there. Basic skill. Oh God.

I'm sorry.

Go ahead.

you know Hello,uh-Action.

Well, What is going on?

You understand? Very nice.

Yes.

I mean, I don't know if I told you or not about that guy. He was renting our old family business. Yeah.

And some, some issues was we're going through with him. So that's why if you notice, I'm working a lot lately from Yeah. Yeah. I still hear it till late, till even like 4 or 5:00 AM in the morning, which is about about maybe nine or 10 hour time.

From here, from there.

Yeah.

Just to be present at the premises, if you know what I mean.

No, no, actually he's still here, he's still renting the business, but we are not on good terms, you know?

We're making sure that he doesn't go back, come back or something.

So he used to rent out the whole place, including an office, including a backyard garden, including a garage. So just to make sure that he wouldn't increase the rent to what's supposed to be as market, as marked a median, if I may say, he said, "Okay, I wouldn't use the office. I wouldn't use the garage or the garden or whatever." And he just, he's literally leaving the trees to die. So I brought in someone to... to take care of the garden, you know.

This was the guy here. He came back just to give me the keys. Exactly, if I may say so, yeah.

Okay, got you.

So you're just there to try and maintain the area?

But it's really hectic because, I mean, I'm working now.

Got it.

Got it. Got it. Okay.

Understood, understood.

Obviously, I won't be able even to go out for the upcoming maybe six, seven hours. And I just make sure that you wouldn't.

because now it's exactly like eight years 8:39 in the evening, so we already finished.

Sorry for that side recap and everything like that.

We're gonna start going down.

We try to make things as efficient as we can.

you're going home.

Yeah.

Yeah, yeah.

Oh, wow.

Yeah, that's fine.

Yeah. Right.

You know, this is really a good lesson because my mom was the person who made the contract with them, the lease contract.

How is it fair?

Got it. Okay.

And we were on very, very good terms. And she took a very critical decision at an emotional point. So she gave them...

I think either a seven or nine years lease, which is crazy.

All right, well, let's go ahead and get into it.

Exactly, no one does that here.

So she did a decision based on her interest.

Let's see what we got here.

Exactly, yeah, as if we are owning the place for long.

I mean, it's pretty much-The same things that we discussed yesterday.

Don't ever make a critical decision emotionally. That's a very...

Yeah.

I really haven't, I mean, I don't live, they're in your office, so they haven't really been too much of a bother, but I mean, I know when they're around for sure.

That's what I'm paying for now.

Yeah, I'm good. I'm good.

Look at the bright side, Josh. At least here, no kids. So I'm focused 100% and I'm more productive. That's how I see it.

Exactly, yeah.

Okay, okay.

Okay.

Let me see if I can get my computer.

Just.

You know what's slow, but that's fine.

I'll go ahead and use this then.

I'm still letting this thing load out.

So while it's doing this, I will...

All right.

I sense you.

Same thing as yesterday, 4019 37th Street when it comes to the policy binder and stuff like that.

I sent it to you, it's the policy.

What does that send over to you?

I sent it to you on Telegram, but I don't know why Uh...

Up till this moment, you look like you are offline on Telegram.

It's fine, but just, I mean, I'm not offline clearly, but I'm just saying what, back on what our topic, 4019 37th Street, Um...

I don't know why.

Beautiful.

He sent us the code.

Let me open it and tell you.

what did he say Okay.

Yeah.

I mean, it shows us they'll receive.

That's why.

Okay.

Yes, sir.

Okay, so the insurance is 150.

Okay, so of course, obviously I told him that he's currently paying 150 per month.

You said their insurance will be 151?

So he was trying to match that. So what he did was 151.13 per month.

full pay that's $824.28 for six months, which is really...

Hokara Shrek.

half of what he Very important.

I think this one here is really good.

Okay, okay.

The interest what?

And then, okay, that's not bad.

Yeah, for the Odo.

Yeah.

Yeah.

Yep. What? What's their house price? $39.44.

Well, That's not bad at all. No, it's good.

39, 44?

That's half what he offered before. And the home insurance, the homeowners, That's 3944.

No, no, $3,944?

62 per year.

Yeah.

That's...

That's it.

Yes, sir.

That's 353 per month.

328 per month Let's break down what's our payment.

Yes, for you.

No, that's that's in case if you're going to pay it at once, won't pay.

Okay, let's do quick math real fast.

But if you're going to pay it monthly.

That's 353.

Pull up everything on...

The property checklist, please.

Okay, give me one second, almost there.

Yeah, sorry.

Yeah, give me the principal interest and taxes.

Okay, P&I?

12:03.

35.

Texas Yes.

So 335.

And then what?

Our taxes?

281.15.

So 1813 is where they're at, right? 1813 with their own insurance, 1813.

Okay, alright.

Okay.

And then...

27.

328 was 328 minus 355 328 minus 355.

Okay, give me a close second. 27 plus 26.

1840, okay.

Got it.

Ew!

Okay.

So What I'm seeing here is that 1813?

There's something that I don't understand.

It says here the full pay,It's 39, 44, 62.

is what their payments would be.

Um.

However, the escrow pay, it's $38,9437.

If we can make sure that our mortgage company will escrow 1813, if it doesn't, Their payments is 1840.

per month.

So does that.

1840. Now,That's it.

SRO. SRO means that The bank basically, the escrow means that it's been paid out, it's been bought all at once.

Yes.

Yeah, I can see you going.

More times than not, escrow means that the mortgage company has paid it out all the way through. The other one is basically, no, Tracy, I'm in a meeting right now. I can't answer that.

I'll answer you in a little bit.

The system already replied back to her.

Yes, I'm not sure if she's trying to call me or if she's trying to call you.

Excuse me, you can call me.

All right, cool.

No, okay, got it.

It's all good. Let's go ahead and stay on topic. So let me go ahead and call Jacob.

Okay.

Okay.

Joseph, sorry, Joseph.

Your call has been forwarded to voice down. The person you're trying to reach is not available. At the tone, please record your message.

Hey Joseph, what's going on brother? Okay, so... 1813.

Hey Joseph, what's going on brother? Hey, I wanted to go ahead and give you kind of a breakdown of what we got back from the insurance company. Okay, so when it comes to the insurance, they did say that you would have to bundle in your car insurance in order for you guys to, you know, basically get approved for the homeowner's policy. And again, I think a large part of that is probably the credit part.

I personally have had it where they did the same thing where they gave me a higher premium because I was seeing a greater risk because again the way that insurance companies make money is by our ability to make those payments.

Home insurance isn't Exactly or insurance in general isn't exactly tied to anything but our ability to pay it back. They usually determine one of the ways to determine what our premium amount is, is our credit ordinance. And so I'm very much positive like the reason why they structure this way had to do with the credit part but it's all good. What we did get a quote back for the car insurance part was 151.

So based off that estimate they chose the, I basically told them exactly that it would be about 150 to 160.

They got it down to 151 for the liability part, which is great. So we got that there in the bag. Now the next thing is the home insurance policy. So what they have are two different types of home insurances.

Now, I wish I could say that we really have a choice in matter, but it goes back to the mind bank, essentially. So here's the thing.

When it comes to your monthly payment for your home insurance, If they escrow it, that just means insured. The insurance is they have one big old bill that's needed to pay it all at once. If my bank accepts it and they say yes, we'll go ahead and pay for this entire homeowner's insurance and basically including the payments back.

That's going to be $328 per month. Keep in mind that's included inside your payment.

Okay? $328.

Now, if my bank says no, We don't like this. We don't accept it. Whatever, right?

then that payment is different.

The payment would be $355 per month. But basically what this means is that it is a month to month agreement. So essentially it goes from my bank paying for the entire policy for the entire year to basically the policy being an active month to month. So that just means in short.

I know that you guys aren't, you guys have been excellent when it comes to making payments, but if it were to lapse when it comes to your mortgage payment for too long, your home insurance could also lapse.

short.

That's the that's the offset when it comes to all that but long story short three hundred and fifty five dollars to three hundred twenty eight dollars This is how it impacts your overall payment so 1813 is what It looks like when it comes to my bank saying yes, we can go ahead and escrow at $1840.

is what it comes out to be when it comes to if it's month to month.

So that's the difference between 27 bucks. So now, like I said, what you're paying for now is a mortgage. All this will be escrowed with a servicing company. We're still going to credit two payments received.

to our third party servicing company to make sure that your balance actually reflects the two payments that we receive outside of their servicing.

Oh.

But yeah, besides that, I just want to kind of give you a breakdown of what's going on. So just to reiterate, it's 8-13, 18-13, if our bank says yes.

we'll go ahead and escrow your mortgage payment I mean your I'm so sorry your insurance escrow your insurance or 1840 if they say no and we'll have to choose the month to month option. But keep in mind this is with you accepting their policy for $151 per month for liability for the car insurance, which honestly is not a bad deal at all. And so let me know if all this makes sense and we can go on from there. All right.

We're talking to them.

Good.

Yes.

Okay. Oh Let's do the... Okay, so next one. Let's go ahead and... So... We got that. all the way. So the thing that I need to add as an updated task-for 4019 37th Street. It's us speaking with Joseph. Speak with Joseph?

Thank you.

you Okay. Uh, Did you send me the actual exact number? The one you said, 18 something?

his new mortgage payment Insurance is escrowed.

Yes, exactly.

and $1,840 if The insurance cannot be escrowed and it's month to month.

And make sure you put the address in there, that's 419 37th Street.

Okay.

Yeah, for sure.

I'm gonna call Tracy right now.

Give Joseph a follow-up call on his new monthly payment.

Thank you.

Hey, did you ever find out how much the escrow shortage was for 2802 South Channing?

I did, but I mean,Thank you.

The updated.

Exactly, no. That's exactly what I was about to tell you.

Okay, let's go ahead and get that real fast.

Not the updated one.

Let's call the mortgage company.

Form on Jose Morelos profile.

Correct. Just like you usually do.

Okay, yeah, yeah, yeah.

Go ahead and pause.

Okay. I'm just confirming.

uh... Authorization.

There we go.

Okay. - Yeah, this is the one here.

informationTalk to you soon.

Hey Tracy. Hey Josh. Did you guys ever find out how muchLeft on the shortage.

I am actually on the phone with Mustafa now. We're calling them, I guess the mortgages escrow company right now.

Okay, so wait, I know.

If I need to put more towards what the check is or lead.

Yeah, yeah, let me go ahead.

I'm going to assume that we might be good, but I'll go on the phone with our about to be on the phone with him here shortly. He just shared a screen so that we go ahead and give him a ring. But as soon as we get that, I can go ahead and text that over to you.

I think it was like, I think, I think it was wrong.

I think it was around like 15, 1500. Bye. yeah let me go ahead and so we're about to go ahead and reach out to them so we You can get that exact escrow shoulder to mount. And we can give that to you.

Yeah.

So right now I think the main so just me speaking candidly what I saw when he came to the insurance it will probably reduce your payment maybe $15 to $20. It does still make a difference for sure, but it wouldn't be substantial for what we're seeing. right now, but I think the most substantial right this second is going to be this part right here, for sure. Okay.

Just wondering if you could get it as low as possible?

Yes, absolutely. Okay, so we got a... Hmm.

Let me see here. This is something else I'm thinking. So we were paying the export shortage. I think I think before we talk about the insurance so pain to ask for a shorter so just That'd be sick. but I'm wondering this, the city is basically stating that your Home, your taxes have reduced. Those dropped. So that means that the taxes have dropped. It also means that short escrow for tax and should drop to Which that should drop it another round as well. So...

Let me go ahead and speak with them. Figure out how much the S-word shortage is for one.

and in two, Tell them that the taxes have reduced and what will we need to give to them to show them what that reduction was.

Because once they receive that document, they reduce the taxes. So that means that you have a shortage and then you have increased taxes.

So you're taking care of the shortage and the next step is reducing the actual tax payment itself. Because right now you're paying for double.

You're paying for an increased tax payment on top of the difference that was not held in escrow.

So let's go ahead and kind of stay with the taxes part because right now the insurance is the weakest impacting thing in this whole situation.

Yeah, no, that's-Bye.

Just whatever is getting in, I can make all the way down. What I need to put towards making it all the way down. It's really a little bit slippery. Got you. Like after all of this, is it gonna drop into where it's like, Thank you. The main store.

Are we ready?

Got you.

Something significant where we're talking about that low-I mean, that's lower than what we have currently. I'm not sure we can get that low, but I would say that let's go ahead and reassess to see what insurance, not I'm so sorry, the taxes, the tax reductions we're going to do as well.

And then we can kind of come back to your drawing board to see anything else. But I would say if there's any way to significantly reduce it such as that, is going to be a homeowner's policy that's extremely low.

That would be the only way to even get anywhere in that ballpark, but I think we can probably get it below $2,000.

There's a chance that we could possibly get it below $2,000.

I think you're being 18, 17. 18. Bye. Like 1800s that it was supposed to be between me and my mom.

I wanna say it was something like that, yeah, I was like 18. before, yeah. But like I said, a lot of it has to be-So that's the data. It depends on what we get as to, so all of this is being calculated based off, so your payments are broken into four. You have principal, interest, taxes, and insurance. Your principal and interest payment, that never changes. But what happens is that over time, right now, you guys...

in probably about two years. The longer you're in the house, more and more of your payments end up switching over to paying more towards your principal. So paying down the house faster the longer you're in the house, in short. But your principal interest payment will never change. You can never get below your principal interest rate. And the two other ones, taxes and insurance and actually I got a third one for you as well but taxes and insurance right nowSo we have escrow shortage and we're losing in taxes. That's good.

The next one. Go ahead.

Go ahead. Thank you, Chuck. Yes, hi. She is at work.

Pull up the mortgage the property mortgage sheet please How much is the PMI for this property?

Okay. Okay.

For 2802 stop training.

As soon as he gets in, I want all this past him and I'll give you a call back, okay? Thank you.

Sorry. No, you're fine. Okay, so where were they at?

Um Okay, I know. All right, so here's the update. So we're talking about how to get it back to something similar to where it was. So your payments on the house was broken into four. It's really five, but I'm going to talk about the fifth here in a little bit. So principal and interest, those are together. Those never change. It's based off the interest rate and what you're financing the property for. So you guys are financing for $180,000 or $10,000 down at an 8.5% interest rate. So that's basically what calculates the principal interest on the amortization calculator. So those just stay fixed.

The other two things we have is taxes and insurance. We're definitely reducing the taxes. And then when it comes to insurance, from what we have received that quote from, it's only about $27 difference, at least from the monthly payment of what you're paying right now.

okay the last one which I almost forgot to mention is private mortgage insurance now what is private mortgage insurance so basically the private mortgage insurance is what was not added to your initial payments before so when your mom and yourself first got into the milk that is something that the first year we had said that we were going to go ahead and pay for that the first year because of the fact that we didn't include it before private mortgage insurance is basically the Just so you guys are understanding, you guys are in a seller finance and as well as a raffle rental mortgage situation.

So that just means that the principal interest that you guys have is an agreement between us, but the escrow, which is basically taxes, insurance, as well as private mortgage insurance, is literally a reflection straight up. So it means that I'm not making any money on the escrow. That's literally basically between me.

Are you in the bank, if I'm just being kind of like straightforward on kind of how that is to be understood. So because of the fact that the house has private mortgage insurance, you have private mortgage insurance. And what is private mortgage insurance? Basically it means that the house was financed initially for an amount less than 20% now.

That's what it means. Every single bank has it. It's just there as a risk of...

And not really a risk, but it is an assurance on the mortgage. It means that if the house goes to foreclosure, the government is saying that, hey, we're going to charge your borrowers this amount, this premium amount per month to to basically counteract the risk that they only put down 5% now when they first got in the house.

So they end up having to go to foreclosure. We'll take the hit.

and cash you out.

And that's basically what the government has in place in order to help more people get into housing.

So people pay private mortgage insurance when you put less than 20% down.

Private mortgage insurance can be removed, but is not removed automatically.

is usually two things that they're needing in order for the private mortgage to be removed. Now this is a general rule of thumb, every lender is different.

But usually it's two things. One, the house has to have at least 20% equity.

Yeah.

So that just means that the difference between my mortgage balance and what the house is appraised for, they usually want to see at least 20, that's that 20% in short.

So instead of you having to put 20% down, they want to see that 20% actually in the house.

So again, offsets their risk so they have to take the house back and they remove the The private mortgage insurance, they know that there's enough equity to offset that.

That's basically what that does.

So it has to have at least 20% equity.

And two, there has to be at least one full 12 months consecutive at the time of, that doesn't mean that they've been in the house for at least 12 months.

It means that from the time of the house, From the date that they're asking or requesting for PMI to be removed, there's been at least 12 months of on-time payments.

That's usually the two rules of thumb. Private mortgage insurance ranges from like 70 bucks to 100, but I'm actually having, oh, give me a second.

Mustafa, how much is the PMI on this house?

You can put yourself on off mute. Did you find it? How much is it?

116.42.

Okay, so right now Private mortgage insurance is $160 per month. How do you mortgage insurance?

$116 per month.

And so that one, so what we can also, when I speak with them, I can also ask them, okay, how can you go ahead and move it? Now again, those are the two rules of thumb. Every lender is completely different. Our mortgage funds are completely different. But I can see what their policy is on removing private mortgage insurance and so if we're closer or whatever it is You can go ahead and figure out what that is, but long story short, I just need to go ahead and talk to them to see what that looks like. So that would be the overall strategy to reduce the pay down to something around $1850 because keep in mind that initially you guys weren't paying the private mortgage insurance.

I had agreed with your mom that I wasn't going to add the private mortgage insurance again until you guys had been there for a year.

And so that's the reason why it was so low before. Okay. Yes. Let's see here. Does that all kind of make sense? So we're going to go ahead and speak with them about escrow shortage, see what that reduces the payment down to. Also want to ask them when it comes to the taxes being reduced and how can we go ahead and show proof the taxes that they're reducing the payment drop down even further since there's no longer escrow shortage.

I think I'll also ask about the private mortgage insurance as well and what that looks like, you know, being removed and what's that, you know, whether or not we qualify or how far away we are from qualify. So on and so forth. And then the last part is probably going to be that insurance, which is just, you know, scraping a little bit off, you know, more in that sense.

I think they will do like a car house.

Oh yeah, there's definitely that.

Yeah, we're doing that right now with the bar.

They basically got a... What's the type of insurance that Joseph got, Mustafa?

Homeowners.

40, 19, 37th. Mike. No, liability. So, basically, yes.

How's that, buddy?

Proto.

Yeah. So we had to do a bundle on his car payment as I mean car insurance as well as the home insurance to get them qualified but in some cases where you're seen as a good borrower or you have good credit or something like that or better credit You know, it might actually allow it where you bundle your home insurance and your car insurance. They'll also reduce probably the premiums on both.

Yeah.

And so that's a, that is an option. I can go ahead and have Mustafa send you over the contact.

yeah.

My name is Joseph. for the needs of all state. Is Joseph with Allstate and Southwood?

Allstate or State Farm? Yeah, so it's Allstate.

Excellent, excellent. All right, well let me go ahead and speak with the bank real fast and then I'll have myself, I'll either send you over a text message or I'll have myself give you a call with an update just so you know exactly what that dollar amount looks like on what's left on the escrow. Keep in mind that you've already made a payment towards it. So that's also factored in as well. But we'll let you know what that gross amount looks like. Thank you.

Of course. Bye-bye. Okay.

Yes, sir.

Uh, So, Go ahead.

Staffa. What is going on? Okay. Yes.

Okay. So you got everything up right now. Let's go ahead and call Rocket Money, please. Give me the phone number. Give me your phone number.

Okay.

Where are you at?

so that we can get this done quickly.

Oh. Here it is. This is the direct number for the insurance team.

I don't need the insurance.

Yes, sir.

I need the home. That was for later. You can go ahead and make a task to give that to... We can talk about that later, about Tracy. Right now, we're trying to reach out to the mortgage company.

That's the direct number for the insurance team in the mortgage company at Rocket Mortgage. No.

Oh, okay.

Thank you for that. I thought we were talking about something different. Alright, go ahead and share your screen so I can see what the.

I got you, man. This one here. Okay.

Yes.

I tried to make a call and merge us together. I didn't know how.

For faster service, you can access your insurance policy details and provide--No, please go back.

Thank you.

Why visiting? My coverage info dot com. I'm gonna shut this door.

If you are a homeowner on this account, press one. If you are an insurance agent or carrier, I didn't recognize the phone number you're calling from. Please enter the 10 digit phone number associated with your account.

This would be the one here.

Pull up Myra's phone number please.

Thank you.

Remember.

In order to protect the property of your account, please enter the last four digits of your-Zoom in, I can't see.

No, sir. Zoom in please so I can see the phone number.

Can't see it. Zoom in further.

Please enter the last four digits of your social security number.

Okay, perfect. Go back to the other borrower's authorization form.

Speak to the customer representative.

Please make a selection to continue. In order to present, please enter the. Please call while I transfer you to the next available customer care specialist. For quality assurance and training purposes, this call may be monitored and/or recorded. Your call will be answered in the order in which it was received.

Thank you for calling the Rocket Market Insurance Team. Oral calls are recorded and may be monitored. My name is Cheryl. I have the pleasure of speaking with you today.

My name is Joshua Weber. I'm the authorized party for Ms. Myra and Jose Morales.

Hello sir, how are you?

Doing very well. How can we assist you today? Yes ma'am, I was needing to get an idea of what their escrow shortage amount was as well as what would the steps look like for them to remove PMI from their escrow payment. Okay, sir, do you have your phone number so I can pull up the account? Of course, yes, ma'am. That's 110263. 7491.

Okay, just one moment please.

Okay, and I do apologize. You said you are listed as an authorized third party under the calendar?

That's correct, yes ma'am.

Sir, thank you for holding. I do appreciate your patience. Now that I've confirmed you are an authorized party, can you please confirm the client's first and last name?

It's M-A-Y-R-A Morales as well as Jose Morales.

you 2980 Thank you and the property is yours please.

That is 2802 South Channing Street Amarillo, Texas 79103.

Okay, perfect, thank you, sir. And we do have a contact, actually there's not a callback number on the account. What's the best contact number for you?

Give me a quick second, let's see which one we've been using. Give me a quick second, I'll pull that up.

So that is 248.

9 to 0 Nine, nine, eight, zero.

Could we do that right after we go ahead and get everything resolved when it came to the escrow shortage?

Yes, sir. You've reached the insurance team. I don't have access to the insurance, so that's the team I'm getting you over to, the client relations team to discuss the shortage I just neededI understand.

Yes, ma'am it is.

Yes, ma'am. All right, perfect. Well, sir, if you don't mind holding for one moment, I will be right back. Yes, ma'am.

okay cool so that was the uh so that phone number So the phone number I gave you is to their escrow company, escrow department. Could you do this? I don't think we have a field for this one. Could you go to custom fields? and Could you go ahead and... Two things, hold up, before you move, right? Go to custom fields under Mortgage, let me see what the folder is called.

I think it's over. Give me a second. Let me pull it up.

Yes, seller's mortgage. Yeah, let's go ahead and put it. Probably near the bottom. Sellers mortgage, is that what it says? So we're now all the way to the bottom, to the end of that file. Seller's insurance, okay, got it.

Put it at the bottom.

Thank you Yes, um so my question was how much was remaining on the Escrow shortage. for this account. I know that there has been, I think a few payments that have been made So I just want to see what the remaining balance look like as well as how we could get the private mortgage insurance removed and what those steps look like.

So 13 on three.

$399.02.

Okay.

Oh.

Honestly, I... Don't. I don't. Yeah, update a number on final. Just bring it up. No, sir.

Gotcha, and just a question about PMI.

Yes, well, right before we jump off, Guess on this topic. How can we go ahead and make that payment specifically would that just be calling back to you guys? here, or would that be something that we could do through the portal? Yes, sir.

Okay, perfect, perfect.

And then yes, the next question was regarding the PMI and how that can be removed or what those steps look like.

So the PMI, all depends on what level of program you're in, right? So currently right now you are FHA is pretty straightforward. Right.

What were those two scenarios one more time?

What was that you said? If there were-Yeah, 190% local value.

Okay, so that's strange.

So are you saying that that's the, so what is it for this one right here?

Which one of those?

98 So that's what we're-That's how much the S-word shortage is.

So, um, I want... Tracy to be able to make that payment.

Yeah, yeah, yeah.

Using the check. Using the check.

So she should have enough money. So she cashed that check. She then goes ahead and we go ahead and we make it through. Door loop. We do have to change the setting temporarily so that she can make that partial payment. or whatnot for that 1172. 11-7-2-98. Makes sense. Yeah, we can. This is pretty simple.

Can you put this as a separate charge?

You can go ahead and ask Thorley.

Thanks for your patience. We appreciate your call, and we'll be with you as soon as possible.

Yes, sir. Yes.

Right now you don't think that I can shoot you a bird for last night?

My name is John. Did they let you know that I was authorized already?

I believe Ms.

Myra Morales last word, her social is 2980.

Yes, ma'am.

So we were trying to see what the steps would look like. on removing PMI, borrowers payment, and what that would look like.

Yeah.

It's breaking out a little bit just as a heads up, but okay. Yes ma'am.

The PMI cannot be used without your time. Cannot be used without your time, okay.

Okay. Is that because they put less than one? That was 90% down. Is that right? Okay, understood. All righty. Well, I guess I answered my question there. I guess I have no other questions besides that. Thank you so much.

Of course. Thank you. Okay, so...

Good.

Okay, so...

Do what?

We need to call him back real fast because I forgot to get... information regarding the taxes on the property. Actually, I'm gonna have you call back. You're authorized party on this one as well, right? Well, damn it.

yeah.

She's texting me right now.

What's the, real quick, get off of that screen. What was the... The phone number for the mortgage company? Just a general mortgage company?

I think it's this one here.

No, that's insurance, brother.

Oh, general number for the mortgage company.

uh Oh, she'll be here.

833.

65. Thank you.

Yes. 2566.

This one.

Thanks, John. Got it.

Thank you for calling Rockingham Mortgage. This call might be recorded using and third party services. To decline recording, press I found your account based on the number you're calling from. Just a moment while I pull up your account. Now I can understand grieve sentences. Please tell me how I can help you. Or, for more guidance, say, "Main menu." Taxes.

Okay, Texas. Let me see if a team member is available to assist you. Please hold while we transfer your call. This call might be recorded. and third party services. Please wait while we transfer your call to our tax team, which may require you to re-authenticate your account. Thank you for calling the property tax. Our automated system kind assist you in getting information about your property taxes.

Enter your loan or account number If you are calling because your loan has been transferred to a different mortgage company, please press 1.

For self-help information regarding tax bills, refunds, and exemptions, press Next slide. To hear the full main menu, remain on the line. Please hold while we connect you to the customer service team. Thank you for calling Rocket Mortgage. Be sold while we transfer your call. This call might be recorded using third-party services. We need to meet a legal requirement by reminding you that we are a debt collector and any information obtained will be used for that purpose.

However, if you are currently in bankruptcy or have received a discharge in bankruptcy, this communication is not in an attempt to collect the debt from you personally. to the extent that it is included in your bankruptcy or has been discharged. is provided for informational purposes only.

Hello, thank you so much for calling from Get Mortgage. Sorry.

This is Joshua Weber. I'm the authorized party for Ms. Myra Morales and Mr. Jose Morales.

Yes, a loan number for this is 110-825-7000. 263. 7491 Perfect.

And is there a B?

Myra and Jose Morales.

Uh, Joshua Weber.

Myra's last board is 2980.

Perfect, that's a good point.

79103.

Perfect.

Now please state why the phone may be monitored reporting using third party services for quality assurance purposes. Yes, ma'am.

So they had just claimed Homestead and so they have a refund check. that's coming in so they can be able to pay for their escrow shortage. But with that being said, their tax their tax amount has been reduced. by the city. So that's just different than what's currently being escrowed. How does that all work when it comes to getting that amount to you guys so that you guys can do an updated escrow analysis?

or early escrow analysis for that.

We do have a department that does take care of that and we have some where we can send the proof that it did go down. Okay. You can do I guess you can do the email.

And then I think the email will be fine. We can do that.

Okay, I have always an Oscar. This is a sample. Correspondence.

Can you spell that for me? Just to make sure I'm spelling it right. Da.

C-O-R-R-E-S-T-O-N-D-E-N-C-E dot C as in character.

Okay, perfect.

I felt that, That main section one more time for me. That's the OS correspondence just so like and you see that's dot C tax see tax at CoreLogic.com. Yeah, if you could spell that out for me one more again, just so I can make sure I can double check it.

Yes, I have O-S-S-M-C-O-R-R-E-S-P-O-N-D-E-N-C-E dot C-P-A-X-S-C-O-R-E-L-O-G-I-C dot com.

Okay, perfect. Just to repeat that back, that's S as in Sam.

C-O-R-R-E-S? No.

O is an Oscar.

Okay, O, okay, that's a start. The first letter is O. Got it. So that's O-S... C. O-R-R. E-S-P-O-N.

D-E-N-C-E dot CTAX@ C-O-R-E-L-O-G-I-C.com.

Yes, perfect. Perfect.

Okay. What should we probably include inside the header? One more similar email.

I'm sorry, what was that? What should we, Include inside the header when it comes to sitting this email out I would include the client's name, loan number, and then the email. I would include the property address, the same information, client's name, and loan number.

Okay. Well, we see something wrong. What, like, tax, what would we call that? Nice update.

Yes. Okay, got it. Excellent, excellent. And this is for the escrow analysis, correct? The correspondence email?

That would be to the property taxes department.

OK, got you. OK. And then we would just call back in and then after that's been received, They can do the escrow analysis. What would they-when you say proof, Do you have something a little bit more definitive of what that is exactly? I just would hate to, you know, scan something over and not be exactly what was needed. Do you know what that would be or someone we could speak with on who can? Let us know what that document would be. What that proof would be.

Our automated system can assist you in getting information about your property taxes. Enter your loan or account number now. If you are calling because your loan has been transferred to aMortgage company, please press one. For some health information, regarding tax bills, refunds and exemptionsTo hear the full main menu, remain on the line.

She literally just sent me back in the queue.

tax topics. Please select from the following menu options. For information on the escrow tax process,For what to do with your current tax For understanding the legal taxes, press 3. For understanding exemptions, press 4. For undertaxed estate, press 5. For understanding supplemental bills, press 6. For understanding tax refunds, press 7. To repeat these options, press 1. Press star. Or to return to the main menu, please press zero or hang up.

We now have the ability to provide you with the requested information through SMS texting. If you would like a copy of the document sent to you via text, please Press 1. To return to the previous menu, please press 2. For detailed information around certain tax topics, please select from the following menu options.

For information on the escrow tax process, We now have the ability to provide you with the requested information through SMS texting. If you would like a copy of the document sent to you via text, please Press one. To return to the previous slide, and you We now have the ability to provide you with the requested information through Thank You. We see that you're calling from 8-0-7-8.

6, 7, 8, 1, 8, 4, 9, 5. Is this number? Thank you. The information you requested is on its way. Thank you for coming. contacting the tax department. To return to the main menu, please Press count. To return to the main menu, please press pound.

Can you speak with somebody? Oh my fucking god. Okay. Of course this link doesn't work. Oh, there is. Okay, so... What we need is, let me figure out what that document is. You're on mute. Okay, let me go ahead as AI real fast. Okay, so we have an escrow analysis that we're needing to do since our taxes have been reduced. We just want to know what document we need to send over to ourAsk the department with our mortgage company in order to prove that the taxes have been reduced.

What's the document name? So then we can ask that from the appraiser's office.

Okay, um...

Josh.

Okay.

Yes, give me a second. I'm just texting Teresa.

What's her-What currently is Tracy's mortgage payment?

Total payment 210383.

I have an AI bot for a real estate mortgage here. It's very helpful. You can ask it whatever you want.

OK.

I just, uh... Oh. What was I saying? Just get that in there. All right, cool. So let's-no, it's all good.

Just a minute, Josh.

This one here. Sorry.

I just need-we're good. We're good. Let's go ahead and get back to our task. I'll give you exactly what we are needing for-For taxes, okay, so for 2802 South Channing, All right, so what we're needing to do is that we need to go ahead and send Tracy over. an invoice for 1172 98 but we're not going to stress ourself out about that she needs to go ahead and cash that that check and she needs to tell you that she's ready for it.

You're not going to send her over an invoice right now. You're going to go ahead and send that. You need to go ahead and follow up with her to see if she's reduced, see if she's cashed out.

Okay. Is it...

See if she's cashed that amount. and if she's ready for that payment. Yeah, so when she's ready, they'll be there for her right now. Let me see.

um Okay.

What is the payment owed right now? 2103? Was there a normal pain?

2103.83.

He won't be able to catch that check anyway until she signs the amendment to addendum and get it notarized.

Yep, that's all I heard.

Yeah, exactly.

So. Just charge on door loop.

I have a question. That amount that you give me, Is it going to be an invoice or an actual charge on Buralukh?

You can just go ahead and do that. Okay, next one. Let's see. Let's go to Notion. Um. So you have that task in place for Tracy. Okay, yup.

Yeah.

So she needs to go ahead and do that. as well as, let's see, Maybe 11. 77%. So 298.

Okay, cool, so 117298, Shortage your file with her on that and we need the tax reduction sheet from the city. So Tax reduction sheet just needs something that shows what the new tax bill is.

What?

Okay.

We can probably get that, but I wanna see if she can go ahead and cash that check.

Us or her? Okay, got you.

That's probably the biggest thing. Yeah.

Right, let's go.

Okay, cool.

Next one.

Let's see. This one, sorry.

I want to make sure that's added.

Okay, cool. Have Vince create an SMS automation for PMO SMS response. What automations are you working on right now?

The skills the skill for.

Uh. The skill for...

The tenant payment checklist and door loop. so that it would check the payments, log into Duraloop, check the payments and update the sheet automatically. I'm way, way past halfway through, like maybe 80, 90% complete. Because it needed a lot of getting his stuff to be done manually. And actually, I'm stuck at a part. I need your help with that.

Okay, what are you stuck with when it comes to the...

Let's go. Um. Let's do this. Let's bring that up. I'm cool with us talking about that, but we do need to go through these small little checklists real fast.

Okay, so we'll talk about the skills, which is beautiful. Let's see, we don't have to worry about that. To find the structural engineer, we don't have to worry about because we're not finding that. property more. Reach out to Esther Cantu. I think I have a meet. I thought I had a...

No, because I called her a few times yesterday and it goes straight to voicemail.

Don't I have something going on today?

Sharon Florida Property Review.

So I couldn't.

schedule there at all.

Oh yeah, I remember Sharon.

I got something like three.

Did you say you have a meeting at 3:00?

Yeah, yeah, at 3:30.

Oh my god, is it 2 p.m.?

Let's see.

Yeah, it is.

Oh my God.

Okay, so here's something else we have.

yeah we were talking about bullshit this whole time okay let's see here Michael so Esther Cantu are we still reaching out to her You have a task for it?

Yes, sir. I'm on it. Don't worry. Yeah.

Yes, sir, I do. uh Mm-hmm.

Okay.

Okay, Michael Boulos.

Is that one inside the document section?

4513 48th Street.

The amendment to contract is it inside the documents?

So send it to Michael and Kenneth, right?

We need to go ahead and send him over to the amendment to contract for that property.

Yes, 4513 48th Street.

Oh, okay.

Yes, that's under the cellars.

Just copy it. on the email.

Profile.

Okay.

Kenneth already has a copy because he had to sign it.

Okay, let me put it in set tasks really quick.

Well, yeah, you can send it to Kenneth just in case he didn't get that, which he did, but, you know...

Okay, I'm good.

Well, he had a sign in, so he got a copy of it.

Next one.

They are awesome.

But just to reiterate, yeah, that'd be fine. So 4513 48th Street, just go ahead and send him over that and Michael.

Okay, let's see here.

Yes, sir.

We just need to put our watermark if you want to, rental on script.

I'm checking right now, 4513 48th Street to see if the pictures came through.

And you're good.

Look good?

Phew.

I can only see it here.

like Three, I guess.

Okay, there we go.

Do they have a picture of the front of the house?

Well, I think just two and one of the backyard.

Okay, there we go.

Oh yeah, I love that backyard picture.

But the tree is just hiding in the garage, you know.

Nice.

Nice.

These are nice.

Yeah.

I'm glad they kept that away.

Yeah.

Yes, from Canaveral.

They're awesome.

Is that right?

It's really good.

Okay, cool deal.

Okay.

Um.

Okay, that's cool.

Yes, I would like you to go ahead andI don't know, watermark?

Actually, one of the skills I wrote down is ordering the pictures.

You know how to do that?

Yes.

Yeah.

Yeah, actually, you know what? Let's go ahead and make a skill of this real fast. I think this is a perfect opportunity to go ahead and do this.

I'll show you how to do that.

Okay, so let me go ahead and share my screen.

So can it be the same one so that when it gets back the It just adds to it right away.

So.

Well remember skills are basically things they know how to do. They can collaborate skills.

So, I'm gonna do this.

So basically this is a whole conversation right now.

Okay.

project so I want to I can add another this is basically that so I open up cloud I guess I'll try this folder.

My only problem with that, I can't give it screenshots when I'm stuck.

This is my only problem with it.

No, which I can.

Okay.

So I want to give it an example.

Real quick.

of what it would be doing.

So what I'm going to do is a few things. I'm going to give you one example.

They say you can't give it screenshots when you're stuck.

Let me save us some time so that we can get this done real fast.

Oh, you just need to click on the first one.

Let me focus like a real fast.

This something, oh.

This works. And maybe this can also do the same thing of--Thanks.

Oh, you know what?

I love this website.

professional and good quality.

Yeah, I think I do a good job.

Show more options at the bottom.

Oh.

because it's compressed.

Trying to...

Trying to.

There we go.

Okay.

And I think there is a way that I can share skills as well, which is cool.

I can actually add on this.

Damn it, did I... I'll invite and delete it.

Usually I have a template that I always use.

I think you saw it, Josh.

You saw it.

Well.

Yeah, there it is on the right side.

That sucks. OK.

It's upright.

Um.

Okay.

Okay.

No, this was over here.

940 by 626.

Yeah, that's fine.

That's perfect.

you How we eat down on this?

Is it 45th Street or 48th Street? Thanks, buddy.

48.

It says 4513 48th Street.

I got confused once. The other one is 4618, 45th Street. Okay. Let's do it.

Okay, let me show you how to go ahead and build all this right here as a as a skill So this is obviously looking at a creative skill.

So I'll say something like this. I would like to go ahead and create a new skill.

So, this is obviously with me knowing exactly you know, What would you like to create?

Tell me what sport, what problem to solve, or what behavior?

I would like you to, I would like to create a new skill.

that would Take...

a file that has images and it will overlay that Image With our logo, for our rent-to-own cribs company The image.

will be 940 by 626.

And the logo dimensions should be 410 by 248.

The transparent background logo will be on top of the image of the house And it will be.

Positioned.

In the bottom right hand corner. of the property All basically how it will work is that I will give you. a file name and the location. And what you will do is Download that file which should have images of a property. You will download those and then you will create This combination onCanva. Each image and overlay with our logo will be made one at a time. and download it into a new file. where all the images Walrus.

The name of the file will be called the property address. will be called the property address and finished.

And that file will be located in the downloads section of our computer file If we do not Explain.

Forehand. where we want those pictures to be placed.

The file.

for our logo and this is for our rent to own cribs Business. The file name is called rent to own cribs logo transparent background and is currently in our download section. I want you to take that picture file And To save it. under a file called Brand. Themes. where we'll keep Are companies branding, This won't be specific to just this company but any company in general will keep all of that data there.

and reference it as applicable. And is applicable. You will ask Ask me questions. such as the file name for the image Where is it located? and where you would like to for me to Have you place completed File at... you can place it in the download section. or you can email this to us. and as well as you can do any custom placements of where we like that those images as well.

We currently have a MCP integration with Canva, so that's where you'll be building all this. So now I should ask us more questions. Clear.

and remind you this is one of two different ways we can create skills so one way we create skill is deliberate by just saying that hey I have an idea of mine I wanted to create a skill and I want you to kind of walk me through the steps or another way is that you just completed a whole bunch of tasks, but you have to be very specific. Hey, you like, for instance, when I built, I forgot to show you, I actually built an app after I was finished with it, or at least I've gotten to that point.

I wanted to say, Hey, you just learned a whole lot about building an app. Could you create this as a skill? You know what I mean? So that's also another way.

I really can't wait to see what kind of questions you ask.

Very curious.

Um.

Oh, here you just say yes and don't ask again. That's what it feels like.

Well, that's fine, but sometimes it's okay to be a little bit more articulate. about everything. So writing skills is great. I'm surprised maybe it already has enough information already. Oh, it's saying that is it cool? Logo brand rent.

Yeah.

Check downloads for local file.

Yes, go ahead and check. downloads for the logo file. However, Once you have this logo, you'll go ahead and then you'll Place it inside of our Claude folder. under a folder called brand and it there for future increase Also I have included a completed file for reference so you know how this is supposed to look afterwards called 4513 48th Street finished.

Get child island? Okay, don't.

Find local files and downloads.

So the name of the Logo. is called rent-to-own cribs logo transparent background You'll keep that. For safekeeping. Under the brand folder. And then the Reference. File just so you could be able to know like kind of how it looks and this is only for rent-to-own cribs specifically so you would want to keep this reference image very specific to just this logo so you kind of know what it looks like and also make sure you keep in mind the dimensions of the main image as well as the dimensions for the logo.

that is going in the bottom right hand corner but the reference should give you all of this Add type.

Get local image dimensions. Mashu Dabbins.

Brand themes. Yup.

One thing that I did want to include is that sometimes the images that we give you To go ahead and overlay with our company logo is not the right size So what that means is that when you upload them into canva that you would need to resize the canvas that the image is going on top of to make sure it is 940 by 646 So to make sure that that image is the right size. One thing that can help you move quicker is by Simply creating the canvas to the right dimension.

And then going ahead and downloading the image on that canvas. And then obviously positioning and sizing the logo where it needs to be. Downloading it. and then removing that image from the canvas, keeping the logo in place downloading the next Image. sizing that to the position of the canvas, keeping the logo in place, and then moving that the positioning of the new image to the back of the logo and then downloading that.

That should actually help you move through this quicker as well.

Good catch on the dimension correction.

Also, make sure you keep in mind that the dimension for the logo should be 410 by 248 and that's in pixels of course.

Okay. Perfect. And now it's ready to go ahead and use a folder.

So I currently have a folder inside of my downloads folder called 4513 48th Street pictures. go ahead and Create. This As a opportunity to add our logo. We're into home cribs. On top of. the set of pitchers, inside of that folder There are Two files that you'll want to ignore which are copy folder to desktop and license. If you click on the second set of file which is 4513483 the image files will be inside of there.

Also, when it comes to that skill, Make sure that you note that when it comes to how you organize Organize or reorganize the pictures inside the file. should be in numbers so if There's 10 images then the pictures should be ordered from one through 10. and it should be in order of exterior of the house meaning the front of the house Then it should go to the living room. Then it should go to the kitchen. Then it should go to the bedroom, which should be the assumed master bedroom.

It should go to the master bathroom. Secondary. bedrooms, secondary bathrooms, any type of additional images such as a hallway or the garage and then the exterior. of the home from the back. So make sure you also add that to the skill and that's the ordering and how you actually upload it to the the return file for the finished product. So Keep that in mind as well as keep in mind that there is a set of questions that should be asked when it comes to the image Wow. Name.

The location, as well as the placement of the completed documents once you're done. But that is the file. I would like you to go ahead and start on. Oh dang it brother I forgot I totally have a meeting right now. It's not at 3:30 it's 2:30. So, I gotta go. So, but that, yeah, let me go ahead and jump off of here real quick. And so I didn't deal with people there. I apologize. I'll give you a call back.

Okay. Yes, ma'am. Hey Sharon. Hey, how's it going? I'm doing well. I'm just getting off a meeting, actually. I'm glad you-you're right on time.

Thank you.

Okay. No. Yes, sir, thank you. Thank you.
