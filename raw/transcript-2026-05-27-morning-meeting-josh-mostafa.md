# Morning Meeting Josh, Mostafa 2026-05-27T12:00:00.000-05:00

*(Pulled from Notion by the notion-meetings connector on 2026-06-03.)*

---

### Property Investment Discussion

- Austin presented a multifamily property opportunity with 8-9 units  

- Low-end cash flow estimated at $408/month with units renting at $850 each  

- High-end scenario: 9 units at $1,000 each with $640/month cash flow 

- Josh decided to decline the opportunity due to current workload: automating rent-to-own business, building commercial cleaning company, and automating wholesale operations  

- [ ] Josh to follow up with Austin once at least 2 out of 3 businesses are delegated  

### Setting Up Claude Code and Skill Builder

- Josh guided Mustafa through installing Claude Code in Visual Studio  

- Created a "Skills" folder structure with "Skill Builder" subfolder  

- Imported skill builder reference files from a YouTube creator (Herc)  

- Skills can be invoked by name using forward slash or automatically based on context  

- [ ] Mustafa to watch Herc's YouTube channel starting from 3 months ago (not recent videos to avoid being overwhelmed)  

### Tenant Payment Tracking System Overview

- Main file: "Property Payment Checklist" with tab "Tenant Payment Checklist"  

- Key columns explained:

- Column A: Property address  

- Column B: Deal type (Rent to Own, Seller Finance, Normal Rental, Section 8)  

- Column C: Occupancy status (Occupied/Vacant)  

- Columns D-G: Tenant names and phone numbers  

- Columns H-M: Section 8 payment breakdown (government percentage, personal responsibility)  

- Column N: Total payment amount 

- Columns O-Q: Payment status checkboxes (Processing, Cleared, Section 8 HUD Payment)   

- Column R: Due dates (25th for Rent to Own, 1st for others) 

- Column AH: DoorLoop ID (newly added)  

### Payment Tracking Methods

- Rent to Own: All tracked through DoorLoop 

- Normal Rentals: Tracked through DoorLoop 

- Section 8: Tenant portion tracked through DoorLoop, government portion paid directly to bank account (Base Lane)  

- Seller Finance: Some through third-party servicing companies, some through DoorLoop (case-by-case basis)  

### Skill Configuration

- Skill will run daily via Claude's scheduler to sync DoorLoop payment status  

- Automatically updates payment processing (Column O) and payment cleared (Column P) checkboxes  

- Auto-populates "Borrowers Last Payment" (Column AB) when payment clears  

- Calculates "Arrival Deposit ETA" (Column AD) using formula: AB + AC (transit days) 

- Skips vacant properties (Column C) 

- Matches tenants using address, name, phone number, and DoorLoop ID  

### Integrations Set Up

- Google Sheets: Already authenticated through MCP  

- DoorLoop: API key provided  

- Telegram bot created: "Rental Update Bot"  

- Bot token configured for notifications  

- Email notifications also configured to Mustafa's email  

- [ ] Mustafa to start the Telegram bot by sending "/start" command  

### Identified Gaps and Solutions

- Section 8 payment verification: Skill will message Mustafa on Telegram and email for confirmation on the 1st of each month   

- Missing DoorLoop IDs: Skill will auto-search DoorLoop by address and populate Column AH when found 

- Third-party serviced properties: Skill logs warning and skips until further training provided  

- Column W (Upcoming/Past Due): Left as formula, skill will not modify   

### Future Enhancements Discussed

- [ ] Mustafa to add summary report feature that emails and texts payment status overview  

- [ ] Future: Add automated text messages to late tenants through DoorLoop   

- [ ] Mustafa to create a list tracking all skills being built (max 3 active skills at a time)  

- [ ] Mustafa to identify and create 2 additional skills based on repetitive daily tasks  

- [ ] Josh to migrate Mustafa's task management to Notion 

### Testing and Next Steps

- First automated run scheduled for tomorrow at 8 AM (accounting for daylight saving time)  

- Manual test run initiated at 2:39 PM to verify functionality  

- Initial test showed DoorLoop property IDs found but empty leases returned 

- [ ] Mustafa to review test run results and report back  

- [ ] Mustafa to not download any external skills without Josh's approval (security risk)  

### Key Principles Emphasized

- Keep skill explanations simple and specific upfront to reduce interpretation needs  

- Creating skills IS doing work - time invested in automation pays off daily   

- Understanding 50-60% of educational content is ideal; if 80% is new, go back a step 

- Check and refine skills daily before leaving them to full autonomy  

- Focus on solving real repetitive tasks, not adding random skills   

### Business Goals

- Target: $50,000+ monthly revenue with $10,000 passive income 

- Current focus on building processes and structure that can be automated  

- Philosophy: "Don't find customers for your products, find products for your customers"  

What is going on, sir? Good afternoon, man. How was your yesterday?

Hey Josh, good afternoon.

It was really cool. So it had been public holiday in Egypt It's some kind of religious holiday. It's like four days, I think, four or five days, I believe. Since yesterday So yesterday, today and another two or three days, People are like celebrating and doing barbecues and stuff like that.

Okay.

Very nice.

So, yeah. some kind of religious ritual. Yes.

Very nice. Okay, excellent. Well, I mean, since yesterday, I've just been pretty much been working on About the same thing really.

Okay.

just, you know, we're here trying to build out this wholesaleUh, acquisition thing with GoHighLevel.

I just want to say how thankful I am. Okay.

I've also been working on skills. since yesterday as well. Now, one thing I heard which helped me out a whole lot is is that skills is like the recipe And AI agents are the chef. Those were, that's the best way that I've heard explain the difference between skills and AI agents.

Okay.

That's so prestigious by the way.

And so, What... Huh?

That's so precise. So please.

Yes, yeah, so basically, What what I'm doing or what I've figured out how to do is how to go ahead and build skills which is really, really good. There is something that I think I need to add to Your, uh... your current CLAWd Interface.

Okay.

Hello.

So it knows how to build a skill and kind of show you a little bit how it works, but it's very intuitive actually once you kind of get it. But essentially, You can do that, but the only issue, well, I guess you can kind of do that in a way.

-So just to tell him, So, clog whatever you have just done, save it as a skill.

You would just have to be kind of specific. Yeah, so you would just say, hey, you just did X, Y, and Z. I would like to create this as a skill. You could do that as well. which honestly isn't a bad idea at all, but I would say to the most part, it will probably be good for you to like go through your task and at least once a day, For us to start building and collecting on skills, meaning that one skill that I'm building right now is, uh... What was it?

Emails.

you Yeah.

I know that I have to look through my emails every single day. Well, let me go ahead and make today about creating a skill about checking my emails. Okay. Let's just say that it's doing... Dondi Cook. Who's Dondi? Oh, Dondi's the photographer, right? You just called me right now, hold up.

you I tried her again today.

She didn't pick me up.

Hey, Donnie. Uh oh, let me put you on speaker, sorry I can't hear you.

She was calling us at the same time.

I have a new lead. I think she's trying to call you.

She's calling you right now. Just calling you.

Keep it connected. Okay.

Hey, Dondi. Hey, how are you?

Hello?

Hey, doing very well.

Hey, I'm so sorry I missed your call. I have been swapped and just now got a chance to return it.

No, you're fine. So we have a property 4513 48th Street. I think we have put a order on. I think we're just trying to see if there was an update.

I'm about to look at one.

This is Josh, but Mustafa.

I think you were trying to call Mustafa.

Perfect. Okay. I think I told you, remember that we have this weird glitch in our system that sometimes when the order gets ten years, it doesn't Come to I think it was part of the SW team.

Yeah.

Okay.

If you can, any time you put in an order, That's great. If you can give me a heads up just so that I know the word "sweep" because I heard that that's what's in the crowd.

Got it. Got it. Okay. So we still do this on online just to make sure we send you over a message.

Yeah, if you can just send me a text and say, hey, I've got an order in. Everything else is great. I just know the look. for it and that it doesn't get sent to DSW without me realizing it and hopefully Who do you think? It's just, I don't know when, and so I'd rather be safe than sorry. Understood.

Understood. Okay. Um, I think the only question I have was I didn't I'm not sure whether or not you guys have received the lockbox code or the it was the front door front door code.

Yes, sir.

If you want to, can you...

That's what they know.

Actually, let me just pull up my notes.

Mustafa, can you pull up that property real fast to see what that lockbox code is?

All right, go ahead and give it to me just in case we don't have it.

Okay.

Perfect. I'm going to stop this pulling it up right now.

Oh, no, no, you're fine.

0-3-2-3.

You're fine. 'Cause I know we had ordered it right before Labor Day or Memorial Day, sorry.

I did not see it together and I'm not going to lie. We have been swamped and the weather has been rainy here. So we've been having to push things to We've been behind already, but regardless, it's just that, yeah, it got sent over to DSW.

No, you're fine. Let's see. So that is 0-3-2-3?

Perfect.

Okay, I have it, and y'all will have it done today and it'll be ready in the morning.

Excellent, excellent. All right, Dondi, thank you so much for the update.

Thank you. No problem. I appreciate you.

Thank you. Bye-bye. Mm, Diane. Bye. Bye-bye.

So I called her a couple of times yesterday.

All right. Bye-bye. That's like everybody.

She didn't pick me up. So I tried her today.

picked me up so I texted her.

Yeah, so now we know.

That's why she to call back.

So that's a perfect example. Like we can create that as a skill ordering through Dondi. and their team, we can create that as a skill. Essentially. So right now, And I think we should probably start every or we should probably try to squeeze that in every single day is to try to add one more skill to what we're already doing.

Okay.

It really doesn't take too long to go ahead and build these out.

I think that this would be considered a type of the Needle mover, did he say?

So we can probably go ahead and bring that up probably a little later after we go over all the all of our updates.

uh yeah I guess in a way yeah for sure I would say that'll be like a mover um I would say that this now keep in mind that skills are different than if you are editing something like for instance like if you're if you're going ahead and needing to go into like like okay perfect example um the checklist the property checklist currently those I mean I think we're about 90% 5% done with the property check, but there's some, you know, Edits here and there.

Yes.

Thank you. Yeah.

yeah.

You can use cloud code in order to help you and assist you with editing that a whole lot easier. Whole lot easier, right? If you haven't already, right? Where you can actually have it plugged into it and already it can be able to edit all the code and stuff like that. It will be a lot more.

it'll be a lot better, right?

Now after it's complete now, what do we need it to do?

Hmm.

Thank you.

Right? So, okay Well, let's just say that we want to have it where it records that our payments have been made Okay Well one way that we can do that is that we can make sure that Doc's at Webber investment homes receives a statement Every single time a mortgage is getting paid So now we just need to tell it that hey when you see the statement that this has been paid Oh, whenever you see a statement that comes in saying that, oh, we missed the payment, you record that over here like that.

And we can create that as we go.

Thank you.

Yeah, we can create that as a skill or, you know, Maybe that there's a way that we can physically have it read I would honestly think that there's probably possibly rather than it just depending on our out Okay, to to fold right on this we can probably have it where it goes through our email and Docs at Web Investment Homes pulls all the statements and basically organizes our statements and maybe collects that and puts it into a Google Drive where we can keep all of our statements.

We can even integrate it into door loop, right? We can literally do that part. Watch this. So we can have it where it takes physical copies of our statements every single month and puts it into a file. Why is that important? That's going to be great importance from when it comes to taxes, right? But then we can have it because right now, Claude is connected to door loop. We can tell it like, hey, we want you to take this information and connect it over here.

Right?

So all of that is what we call a skill, right? That entire thing that we just explained is a skill that we can have it do. Now watch this.

It going ahead and knowing how to pull the mortgages, that's one skill.

knowing how to then go ahead and check door loop for the for if the Tenants have paid. That's another skill. It going ahead and knowing whether or not what subscriptions we have. That's another skill. It knowing whether or not accounts have been paid.

Whether we've indicated, hey, whatever way that we want to let it know and inform it.

you Mm-hmm.

Yeah.

We do. Yeah.

Maybe we have some type of route. Maybe you have a simple browser where we say that this account is old to this account and this and we click submit and then boom, it populates the goals over here. Right? Then what we can create is an AI agent that in that incorporates all the skills into itself where now it knows what to do with that information. Right? So now we can probably have an agent that's over that entire sector itself.

That's over that.

You see what I'm saying? Whatever that would look like. I don't know yet, but I would say that the first thing that we can do is collect on skills. Add as many skills as we can, and then later on, once I educate ourselves, I don't want to really look into AI agents until we build skills out.

Because once we built the skills, then all we have to do is to say, hey, could you go ahead in your job now autonomously is to read through all this and to inform us.

Yeah.

Amazing. Too good to be true.

So, for instance, if we end up finding out that, hey, one of the tenants have not paid, we want that to go into our notes. In short, it will autonomously do that. Oh, it knows how to now look at that information and maybe be able to text that individual and say, hey, we notice that you're behind on your payment and it can do all of that even more. We need to start off as a skill. Yep. How are you feeling about that?

Yeah, he was overwhelmed with the possibilities. Let's go, let's go.

Yeah, I mean, that's a dream come true, man.

Okay, cool. I think I need to... Possibly plus one. Plug in my computer.

You know what? I think that one day in the past, we didn't even... cross our minds or dream of what we have today in terms of AI agents or workflows or automation Thank you.

I mean, like, yeah, I mean, like I said, I knew that over time this was going to happen.

I just knew that, you know, as I already know how I am. It's like, I just need to tinker. That's all I do. That's like, I know how I am. I just need to tinker. I just need to figure out how it works. And as soon as I figure out how it works, I'm going to learn something every single day. So that's literally how it's working. Okay, cool. We'll get into the skills. Let me go ahead and also add this to...

because I don't want to forget about this. Let me tell Claude to to add this to my daily task actually. So I'm going Task Organizer. Okay, so something that I want you to add to to this task, as well as every task coming up, especially during This is for my afternoon meetings with Mustafa.

At the end of our meetings, we're going to discuss what Skills. We want to add to our Claude code. so that we can help move our own personal needles we'll review the skills that we've already have done. as well as the skills that we are going to be creating. So we're going to talk about that during our afternoon meetings. Also pleased to remember that each one of my Task. Need a. Time limit next to them.

so that I can be able to see how long each one is going to take. I see a few of my tasks that don't have this. Actually, I take that back. I see exactly what you did. You only created time segments for for the Joshua schedules, that's fine. So perfect example, my task here, like my daily tasks I can create a skill instead of having to go to this one No, only worry about the afternoon meeting with Mustafa and what we're doing with the skills.

And that's it. Go ahead and add this now.

Now I'm locking into the rules. Okay, cool deal. All right, let's go ahead and get things started. Oh, eight minutes over.

So this for five. First one. This is have Jacob create a policy binder for 419 37th Street. How are we with that yesterday?

I did speak with him and he said, Oh, actually, Jacob was not in office.

So I spoke with Zach. He's a colleague of him. And Zach, he said, You will need to check the old policy that Jacob has prepared because I gave him the details, which the one which is, I think, nineteen hundred ninety one years. for six months or so. I told them about that. liability, car insurance. that Joe It was a half of 150 per month. and what he can do for the sake of having Having both, he said he will prepare it and send it on text messages.

I had a look, but he didn't send that yet. So, Most probably that would be one of my early follow-up calls today.

Okay.

Okay, do you have a task specifically to follow up with Jacob and/or Zach?

Yes.

Okay, perfect.

Um... 4019 37th Street, also for door loop, did we update his, the amount that's showing on there.

Yes, 1674 something, I did.

I updated it on door loop as well as the tenant checklist. And also for Veronica, in terms of Amount of 100 and date. Change the date from 25th to the 1st on the checklist and go.

Okay.

All right, next one. Follow up with Tracy on 2802 South Channing Street.

I spoke with her.

She said she will do it as soon as she can.

Signed and notarized, what do we got with that? Okay.

She was a little bit busy yesterday. Uh, Yeah. And she said, uh, I mean, I just made it simply clear that she won't be able to cash the check unless, uh, She's I mean, she was very weird.

And I'm not sure, like I'm like...

Well, as long as she makes her payments, it's up to her whether or not that means anything to her. That's it.

She's asking, this cash, this check is just sitting here. I'm not doing anything with it. Should I send it to you guys? I thought it wouldn't really make a difference because by the end of the day, it doesn't matter if... Exactly.

You can't cash it.

I can't cash her check. It's in her trust. I don't know how to, I don't care to figure it out.

Yes, sir. You're right. So.

Is that up to me? That's where we kind of leave the difference between what she's willing to do and you're in the right mindset. So that's perfect. Okay, we're going to follow up with her. Well, since she's taking her suite behind time. On that one, I'm not going to... We're going to leave that. I'm tempted to let her handle this on her own.

Yeah.

I just give her a day or so and fill up her Okay.

Thank you. Let's do it. Yeah, I'm willing to probably start on this on, Friday. Follow up with her on Friday.

It's 30 what? Oh, okay. Okay.

Okay. I'm so excited.

Give me one second, let me put this here.

I got some automations for you to do, man.

Let's do it.

I got some. Yes, ma'am. There's some automations for you to do, man.

Let's do it, my man.

Okay, I'm ready.

Next one. is We still have to do this one. I know that we have to finish it out. I have been to create an SMS automation. for the PMO SMS response.

Go ahead. Provence? Okay.

Yeah, now that we have to do that. Let's see here, what else do we have? We don't have a whole lot. Let's see, status of insurance 419. I think we already did that one. Let's see, reach out to Esther Cantu, or reschedule Esther. Did we ever reach out to Esther? Can't you?

I mean, it rings a bell, but I can't remember What is she connected to?

This was a cellar. I know you spoke with Yvonne.

A seller.

Yeah, that's it for today.

I did, and it's catching up with me.

No, it was Friday at four. Yeah. Esther, I think we spoke together once. I just really can't remember any details. So what was it task related?

OK, got it.

Confirm or reschedule? Yeah.

Yeah.

Oh, confirm on reschedule?

Okay, let me have a look.

We're supposed to be speaking.

But Wendy, you should meet her.

I mean, I'm open to meet her at any point, like as in, you see, I'm available.

No.

But you have access to my calendar, right? I think you do. Yeah, not tomorrow.

I would say Friday I'm available.

I mean, I just see the... The box... Ready?

Listen. Yeah, because I don't have a meeting with Yvonne.

Yeah, I figured that.

I can meet with her at like 2:30.

Okay, let me put this here, task.

You said Friday or tomorrow? I'm sorry. You prefer Friday or tomorrow? For Esther. Okay.

You said what?

Friday.

All right, we have that one, please. Thanks, everyone.

And that is pretty much it for that one.

Okay, next one, 4513 48th Street.

This is for McKenzie. Yeah. 4513 48th Street. 4513 48th Street. I can't remember what that one is. Oh. Plumbing prior to, well, in case you know we're marketing. Okay, yeah, we need to get the pictures back. for that one.

That's the movies.

I do have a task for that.

So we just need a task to check out the pitchers for 4513 48th Street tomorrow.

Let me just casual.

Okay, cool. Good to go. Next one.

Okay.

Next one was 4302 East 61st Street. I don't know whether or not I've heard back from Mackenzie on this one. She's supposed to be reaching out to Jalissa. on them transferring to seller financing. Have we spoke back to McKinsey at all?

Mm-hmm.

I did. I last time I spoke was Yesterday, I just confirmed with her the situation for, um, Veronica, as well as Ashley.

And then she was in a hurry. So I told her, I'm going to call you back. because I wanted to discuss the 4302 situation with her as well as the late payment or that payment for Ronald. So I called her back twice and she didn't pick me up. So I texted her what I needed exactly from her regarding Ronald and Julissa and Justin. I did not hear back from her. I did call her now before the meeting. And also she looks like she was busy.

Okay.

Okay.

I was about to text her again. Excellent.

Oh, McKenzie, McKenzie, McKenzie.

She's very weird. She literally vanishes, you know? Like, she's not... There.

Okay. Well. We're probably going to be creating AI agent here in a little bit.

Sometimes.

It's gonna be replacing you. Careful.

you I mean, I don't believe... And, you know, agent could replace her because she's also doing a lot of manual work.

What did you say?

Yeah, I mean, she'd go out there, she'd meet with people and stuff like that. Yeah, yeah, yeah.

I mean, do we need her to meet with people? Like, for real? Do you think so?

We don't need her to show a property.

Of course, in some situations, if we are marketing for a property, we would need it for walkthroughs.

So. Like the way that it could work now I I like her I like between having her there and not having her there does it help 100% and But we can automate that entire process.

We can literally have it where an AI agent is responsible for essentially qualifying. That wouldn't even be an AI agent at that point.

Okay.

I would think it would be a public set of skills. where it will be put in place to, well I guess yeah it will be an AI agent but, I'm creating an AI agent now to speak with agents. We can create an AI agent to go ahead and qualify people as well, where everything is agentic, essentially. where them putting up their deposit, it being marked as unavailable, Like all that is pretty much ran by an AI agent.

Yes, Yeah.

I can have all that. And it's the only difference will be is that we'll go ahead and put a code I'll put an access code for a change after someone's meeting.

Hmm.

And they'll talk to an AI agent that will go ahead and assist them with all that, we'll just put certain rules in place.

And so, Yeah, we don't need her to show the property. No, it helps 100%. It definitely helps. I can just have it where she clothes. We just need to talk to people. Essentially.

Yeah.

uh Yeah.

I just need to talk to people. -Yeah, so,Well, She's very hardworking.

I get you. I just know how hard of a worker she is. You know what I mean? She's a beast. Yes.

I need her available. That's the biggest thing. And honestly, like... That's why I need her available if we're putting her there. I need her available. But like I said, I'm gonna let time continue. Um... That's pretty much it. I'm just going to let time continue to go ahead and do what we do. Um... yeah I'm not saying I'm not saying that we're gonna let her go but our relationship might evolve you know where Instead of her doing property management for us, we might say, you know, hey, we can build a property management company together.

'Cause that's something else I was looking at is that if we get better at managing our own properties We say, like, hey, we would like to... Build a management company with you. you know, where you're over, where we, you know what I mean? Like we're going to need people. to do that.

That seems...

I feel like we're, we're, uh, perfectly or effectively managing the properties we have in hand.

So that's what I'm thinking So I'm okay with our relationship. 100%.

Right? Yeah. Thank you again.

We're figuring out how to be more Yeah, it is time for us to go ahead and put some skills together, though. because it's time for you and I to both be able to focus on more Different tasks, I wanna have it where the finances are taken care of by AI, follow ups with homeowners or people are done with AI.

Give me...

And even down to like sending out letters and stuff like if people are continuously late now if we get to that point where hey We need you to call this person.

to let them know that, you know, hey, they're pretty behind. We need a person now. But like I said, I'd rather have her for closing on the deal with people, which you can do on the phone, right? Or just even with meeting up with you, that's cool too. And I will also like her for worst case scenarios.

Zlink.

Where, you know, if someone is not paying Exactly.

Yeah.

Okay.

Okay. You get you.

I have a question about this. Where are we with the... What is it called? The BNB.

The what?

The BMP? Airbnb.

Oh, Airbnb. Oh, you're talking about the properties? Oh, man, honestly, it's going ahead and the more skills we do, the more I can be able to focus on something like that.

Yeah.

Okay.

Because right now, I still want to do all of it.

I want to do all of it. But we have to continue to automate. So the thing that I'm focusing right now, we're focusing on, I do want to do that. I want to do a lot of shit. The thing that I'm focusing on right now is I need to build, well, right now, I'm actually building it right now on this screen.

Angels acquisition pipeline or like basically it finds deals for him and basically all he does is you know Speak with homeowners, speak with buyers and assign those deals. That's all that I'm looking at, right? That and then as well as I am, me and my girlfriend, we're building a cleaning company as well.

He's building that.

Uh, You know, and again, the whole purpose of how I'm looking to do all this is I need it agentic.

Thank you.

Oh. Cleaning company? I didn't know that.

I need it to be where it's, I can build it and then it can be handed over to someone else. So I know one thing I was thinking about is probably having Mackenzie over the girls. She already owns a cleaning company or whatnot.

How about we structure something where she's over...

Okay. Wow, okay.

Yeah.

Like she currently has a cleaning company.

For our Airbnb, She has a cleaning company. Yeah.

She cleans other people's Airbnbs.

And so If I can be able to say, "Hey, we wanna do everything.

Wow.

Okay.

We wanna do clean Airbnbs, we wanna clean commercial buildings, residential, all this jazz, and we need you over in charge of the girls." And just making sure that you're teaching them based off of the rules that we have in place, you know, X, Y, Z.

I mean, that's something that we can expand, you know.

Yes.

Yeah, cool.

Hmm.

The whole thing that I'm looking at is that I want to find more ways for us to make active income.

on top of to help support the the bigger things that we're trying to do as well that's that's what I'm trying to do so I want to create them put someone in charge create them put someone in charge create them put someone in charge I'm not looking to be the owner or manager of these things I want to put someone in charge so wholesaling angel if we're doing was it called the cleaning company McKenzie or my girlfriend you know someone like that Airbnb obviously McKenzie I'm just in the background as like the owner or just the moderator.

Thank you.

Yeah. Got it. That's what it's not. I'm sorry. Remember when I told you about maybe 10, 12 days ago, and I told you if we could close at least one wholesale deal a month, because it felt like a along with our passive income, if we could give it a little push, steady, steady, little push every single month The wholesale deal?

Definitely, they'll make a difference.

Okay, so we do Oh yeah, no, absolutely.

Mm-hmm. Okay.

So that's what I was looking at doing. I want to go ahead and have the wholesale company or the wholesale business is more like active income for, business, right?

The cleaning company is active income for me.

So I don't have to eat off the business.

Wow.

So if I make money off of the cleaning, I can leave. I'm one of the biggest expenses of the business, to be honest with you. You are too. You and me are the biggest expenses the business has. So if I can make sure I'm taking myself away from the table where it doesn't have to support my lifestyle and I have something completely away from it, I can let this thing grow all day long.

Okay. Got it. Yes, sir. Wow. This is beautiful.

Let's do it, let's do it man.

I could watch $20,000 drop in that account and I don't got to worry about touching it.

You know what I mean?

Thank you.

30,000, boom. Whatever that is, I don't care. Leave that alone. I'm living off the clean ladies.

Bye.

Yeah, hell yeah.

All right, what's next?

Eight, nine, eventually 10 figure operation.

Excuse me.

Okay, cool.

Hmm.

The next thing was this one right here had to deal with 13 14 65th Drive I'm not sure whether or not we should buy that Right now I got a whole lot I'm dealing with right now.

There's a whole lot we're building. I'm not sure whether or not we should buy these units. It's just... Even though I want to. I want to buy those units next door, but I don't think right now is the best time for me to do it. A whole lot. I know what the bandwidth of fixing a house is. I already know what that's going to be like. And I do want to, but I don't think right now would be the best time for me to do it with how much I know that we are like if I if we already had.

skills in place, if we already had agents in place, if I already had the cleaning company in place and that's already somewhat has some medium momentum, if we already have the wholesaling and that's moving with some medium momentum and now all my lazy ass is doing is checking in with people, we got money coming in. And I got some free time. Sure. That'd probably be great. But right now I'm on the building stages of some other stuff that That's not going to do nothing but drain from our time, essentially, right this second. And even though I want to, I don't think I should.

I really want to. I really, really want to. And I do believe it's something I can do. I don't think it's something we should do right this second. I would say that we're close, but I don't think we're... So nine unit.

you Is it?

Wow, okay.

Yeah, it's a nightmare.

But it needs a lot of work. There's a lot of work behind it. Um... Open this up.

Is it expensive?

So. Oh yeah, I mean, it's probably going to need at least $150,000 of work for sure. I mean, for material and stuff like that?

150,000 for work? How much is that?

Yeah, it's just like, let's say at least 100.

Oh my goodness.

How much is it worth? Emelian?

Zero question. Low, four, Lowden, 408-640.

Depends on how many, it depends on like the low end means that With each unit running out for 850, that's low end.

Oh, okay. That's not bad, I think.

And we can only rent out eight units. Like, because there's a unit in the back, but I'm not sure whether or not we can salvage it or not. So worst case scenario, I know each one of those units can rent for 850 because the person down below me, unit A, Stephanie, she rents out for 850 and I can easily get someone to place her rent in the second.

So I know each one of those at the lowest can rent for 850 and at the lowest I'll only have 8 units. So I know that, you know, look at the calculations for the very worst case scenario, 408, that's the low end. High end is each unit really I have nine units running out for a thousand dollars each and then with the lowest amount of expenses That's bring it to 640 sold 408 640.

Okay.

Got you. Of course. Okay. We need a lot of time.

It's kind of the whole entire range Because multifamily depends on the cashflow. Okay, cool. Let's get back on.

It needs a lot of time. Yeah, I think I completely understood my time. Yeah.

Let me go ahead and...

Little text awesome.

Okay.

I was a hey Austin I'm not sure that I could purchase the units right now I understand my workload I'm automated I read to own business building a commercial cleaning company and automating the wholesale site as well once two of these are Our delegate at least wants to have-Two out of threeAll of these are delegatedOut.

be able to focus on a large acquisition like this one is up let me see I'm going to Try to rewrite this. Hey Austin, I'm not sure I can purchase the units right now. I'm under-estimating my current workload. I'm auditing a rental owned business. I'm building a commercial cleaning company. I'm also auditing the wholesale side. Once two out of three of these are, these two, As a delegate, I'll be able to focus on a significant acquisition like this one.

Acquisition like this one, the opportunity is still available. I follow up with you. to follow up or vice versa.

Okay.

I'll just say hello with that.

Okay, sorry about that taking so long. I just gotta send that message over to... Mr.

Okay.

I'm going to send you over this list.

Pause. Automation. Or did this one? Build an AI finance agent, test AI content builder. Yup, connect AFNO meetings to Vince via Google Transcriptions. Billing in any in-fog email support, audio playback. I'm billing that right now. Set up Joshua profile, observe living document. I've gotten that one actually. Jesus. Set up news briefing. I've actually got that one already. Set up morning video recommendations. I actually got that one already.

Wow. Build SMS notification process.

SMS modification.

I'm not sure what that means. Once we got one off. Thank you.

Have Vince auto update master prompts based on info gained each day.

That's something I can keep. I speed to lead integration to go high level. I'm kind of creating that right now. That one's actually a part of the first one.

You told me you have a dessert for me today.

What was that?

You said you have a dessert for me, like an animation?

That's what I was gonna know I was saying that we was going to go ahead and go over the skill like of us building a skill.

Yeah. It's closed.

Oh, okay.

Okay, who do you owe? Let's go ahead and build one together. Let me grab something.

Okay, I gotta get that's another investment I'm gonna have to get here soon is another desk Okay, let me go ahead and...

Okay.

You know, it didn't do that. This is the same camera. It didn't go up and down.

I really wish you get back that camera that, uh, Went up and down. What?

You keep saying that. My desk went up and down.

So what did it go up and down?

Something went The actual desk goes up and down?

The desk when it's been, no, it's been like two years. You might have forgot the literal, this desk had a motor. It had a motor on here. The fucking dogs chewed it.

I didn't know that.

Oh my God.

They chew the wire. Yes, this death rose. This death can rise. It literally, only thing this thing needs really, because it has the electrical components, the only thing this thing needs is the motor.

Why didn't you get it?

I'm not trying to do all that.

Yeah, no, I mean, I probably do need, like, I really want to, like, there's a motor right here.

I mean, if it were you, I would do it. It's beautiful. It's worth it.

Excellent.

Wow.

It has all the components, yeah. It has a component still. Yeah, it literally just needs a little motor and needs to connect to it.

Okay.

And that's pretty much it. Yeah, if it has a motor and I can connect it, this whole thing will rise up. You know what?

Wow.

Okay. Let's go.

You might be right, but not right now. All right, cool. Let's go ahead and add a skill or the skill builder to Yours.

Mm-hmm.

So what I want you to do What I want you to do is share your screen and while you share your screen, While you share your screen, I'm going close enough on my end.

Okay.

Where to go from here?

Yeah.

Getting it right now. Let's see. I need to get-I got sent you over the file. Go ahead and open up the... The visual thing, I forgot the name of it.

Okay.

Visual studio. Phase one.

Yeah.

Okay, let me go ahead and... Let me get this file. Skills.

Where's my skill learner? Where's the first learner? We're still builder. Let's see. Quad. Give me a second. Hot open. Skills... Skill Builder. Share.

Okay.

Let me see. Rebuild and file export open images. Finding folder. Okay, you know what? I'm just going to go ahead and go into skill. I'm going to go here. Let's say... This is... Classroom. Skills, there we go. Still MD in references. Excellente. Okay, where is it? Download. Downloads. There we go. Go ahead, I'm going to try to paste this in the conversation thread. I guess I gotta select the files.

Thank you. Here. All right. Upload. Reference.

Okay.

Oh, can I do one file at a time? Yeah. Okay, go ahead and download both of those please.

Open.

I just did.

Just download on your computer. Thank you. We did? Okay, good. All right, and then inside of this, I can need you to open up.

Let me see your screen. Yes, that's fine. Alright, I'm going to type in I would like You need to help. Great. is Give me a quick second. Click on-let me see where I can get you to open that up.

Go ahead and click on and right below where it says file there's something that says folders.

Click on that? No, no, no, no. This file is in the top left corner.

Top left.

You Here.

So right below that one it shows a bunch of papers. Nope. It's to the left. Nope, nope, nope. It's not even on that.

Yes, right above the... Yeah, that one. Yep, click that one. Nope. Right there. Yes, sir.

Oh, you don't have a folder. We need you to have a folder. Okay, so click open folder. Okay. Click on the WS-Cloud. No, no, it says cloud right there. Click on that one. Uh, Let's see. Click select folder. Don't click on nothing in particular. Just say select folder. Don't click on nothing, just click a photo and there you go. Boom. Right there. Excellent. Yeah, that's exactly it. Go ahead and minimize that please or exit or something.

Yes, I trust authors. Perfect. I'm not sure what it's doing. Next thing I want you to do is click on where it says "Cloud" in the top right hand corner.

Yep. I'm going to click X on the other one where it says welcome. Perfect.

Now go ahead and inside of, go ahead and copy what I just gave you and put that inside the It's right there. Perfect. And then go ahead and click enter. So right now we're telling it to go ahead and create a skills A skills folder and a skill called Click Yes. Yeah. So right, if you look on where it says Claude on the top left hand corner right there, do you see that?

This one?

Yeah.

So that right there is actually a live look inside your folder, inside that folder on your computer.

What this is doing is that it's going to create a section called skills. And then the first skill is going to create is called skill builder. And this is what we're going to, we're going to actually going to give it. the prompt Just click yes.

whatever it needs.

Has been successfully added.

Um, I don't see it yet.

Here it is.

Okay.

Just put I don't see it yet over how can I view it just put no tight Oh, you see it? Oh, click on the drop down. Should say skills builder in there. Yep, perfect. Now, that's just the folder. Now we have to give contents to it, right? Um. So go ahead and say, But don't click enter yet.

Just say drop both files into that Skills Builder folder.

Instead of all, put both. put both of these so instead of all put both of these and do not click enter both of these excellent do not click enter go ahead and click on the plus icon and add both those files that it gave you. to that.

And go ahead and click enter or send. So now adding the skills builder so what this is you remember how I told you how There are certain processes that we need to use when it comes to creating anything, right? We were talking about that. This right here is actually adding that skill into your computer right now.

Could you tell me a couple of...

maybe channels or something that I can work on in my free time so that I can be more aware of this happening.

Now the thing is, skills can be added in two ways. We can add it from like a source like this. So this is actually from a YouTuber that is really good at doing a whole bunch of AI stuff that I really liked how he built his logic. And so this is adding it to your skills and two, we can create it as well. So we can upload it as well as we can create it.

Yeah, on YouTube.

Channel?

Like maybe the main or two, three that you follow or, um,Okay.

What do you mean? Yeah, I think the best one. I'm going to give you the best one.

Yeah, yeah, I got you. His name is Herc. Let me see here.

Okay.

Oh. Wonderful.

Nate Kirk. No, just continue. Yes.

Okay.

Yeah, I was just going to. Right.

Can you text me his name? Can you send me his name? Oh, awesome. Okay.

So that one right there, I would say you would need to start. Do not watch anything he has recently. If you watch anything he has recent, you're going to be lost. Start off three months ago.

No, I'm being serious because he posts so often and he's so advanced.

Got it.

I would start about three months ago.

Yeah, but on the other hand, you cannot binge his information. You can't binge. I'm trying to tell you, you're going to be overwhelmed. The best thing that we can do is...

From where we are, Figure out what information we're missing from where we're at and then once we understand it, then look at new information where like, oh, I think I can understand that because if 90 to 80% of the video you don't understand, you need to be on the step before that.

Okay, got it, got it, okay.

Okay.

I'll give you a minute. Mm-hmm.

Okay.

You should understand at least 50 to 60% of information that he's giving you and the remaining like 30 or 40% should be new information. But if 80% is new information, you need to go back.

So right now, So right now what it's doing is that it's supposed to be He's reading the description and all this different type of stuff.

Got it.

And so, um...

This is adding the skill builder. So this is going to help us when it comes to creating skills.

so whenever we say hey can you create another skill for me is actually going to look at the skill builder and then be able to build skills off...

Yeah.

It's going to be able to ask us questions off of that.

Okay, let's see. Both files are in place.

You can now invoke skill...

Skillscotch Builder.

You don't have to worry about actually knowing the actual name of the skill. So you see how it shows Skill Builder has two reference files right there.

Yeah.

So basically there's two ways that we can invoke a skill, right, when we actually want to use in the future.

Okay.

One is that we can actually literally call it out by name. Like if you do forward slash skill builder at the end of a request, it will know, oh, I need to use this skill in order to invoke it. Or two, and you could just within context of whatever you need it to do, it will look through the skill builder first.

to first to be able to see what skills is currently there that is the most relevant. So meaning if we have a task for how it goes through the emails, it's gonna look at that, it's gonna see, okay, is this skill relevant to this task?

I mean, arranging the tasks.

for you. So you don't always have to remember all of it. All right, cool. So now that we have the skill builder, Let's go ahead and brainstorm.

Using cloud. Yeah.

on what we can be able to train it first for a skill for you.

If it's time for payments like around 25th or the 1st, Every day I check on the payments.

So think about your task right now. What's probably one thing that you know that you do every single day?

Just one thing you do every single day.

Are we on time?

Thanks.

Okay.

But I mean, if we're all paid, so. I didn't do it up until the next cycle.

Okay, arranging your task.

Okay, um Hmm.

How can we go ahead and insert that?

Okay, so you know something?

Okay, yeah.

We can go ahead and We can go ahead.

and Create a skill.

where Il-Chek Dorlu and then it will update the Google sheet for the tenant part Very simple skill.

Yes, we can do that.

I mean, none of all of our payments go through a loop, but majority does so.

Okay, cool.

and actually go ahead and invoke this skill.

Um, So let's do this.

Let's open up a new chat window real quick. So the way that you can do so is that we can, you see those little three dots next to, not there, that's for like the, that's different, no.

Okay.

Oh, there's one.

The other three dots, this is the next three dots to the left, one more set of three dots.

Yeah.

Uh, so... Oh, I guess I'd be wrong.

Try that one. Yeah, that plus icon, new chat.

Yeah.

Oh, you know what?

I was told to actually make sure that when we're speaking with Claude to make sure we're on the terminal window. So go ahead and actually click X right here.

Click X.

And then click on the terminal, which is right next to help at the very top of these. It says help, terminal, it says, there you go.

Let me turn it off.

Perfect.

Now full screen it. You don't got to worry about that. Click X on that. So full screen right there. Perfect. Now the thing that you need to do is click in Claude, C-L-A-U-D-E.

Then enter.

And then it's supposed to be logging you into Cloud.

And then it basically is telling, saying that you, it's gonna work within this window.

Yes, boom. All right, so this is what we call the terminal window. So what this is, is a little bit different than where you're at before. This adds a lot more context so we can see everything that he's thinking about from behind the scenes.

It asked me to do it.

Okay, so I believe right below, right where it says welcome to the Cloud Code BS or whatever, You should be able to start typing.

It's Ken, Ted.

It asked me to do one of few actions here. So either command escape or quick launch.

Right about it.

or Ctrl+Alt+K to reference files, or just press Enter to continue.

Just start typing.

Just start typing for me.

You can't type.

But have context of open files and open files.

Is he there?

Okay, Ctrl-Alt-K. Control off here. That doesn't make a lot of sense, because I've literally been on that same thing before.

To reference files.

Okay.

Okay. Does that make sense? Go ahead and start typing. Try to type. That's it, yeah.

That's literally what I was talking about. Okay, perfect. So what I want you to do is that I want you to say, hey, basically this is what I want you to say in short. You're gonna talk to him. I want you to tell it is that I want to create a skill where I'm going to, where, How many days a week do we check for the Uh...

I mean daily, for example, today is 27th.

the tenant's payments.

Okay.

Keep checking daily to those ones due on 25th are paid and so on.

Hmm.

Let's do this. Open up Claude from the bottom. We're going to have Claude word what we're trying to say. So what I want you to do is that go to chat please. Okay, so Just put later. So basically just say something along the lines of that, I'm looking to, I need help on how to word, this worth is. Basically, in short, we're trying to create a skill so that we can be able to So, Check. on if tenants have paid.

Okay.

Thank you.

Um, the certain the And I guess the...

Systems that we use are Google Sheet as well as DoorLoot.

So that's perfect. So and obviously I want you to keep so just put actually, you know what, go back to the terminal.

that we were just at and just say that to him. Just say, I want to create a sheet, I create a skill where it will help me with keeping track of our tenants payments We currently track our tenant's payments on door loop.

Okay.

Okay.

as well as Google Sheets.

Okay.

Remember, you can talk.

OK, perfect go ahead.

The systems that we use in place are Google Drive. and door loop.

Okay, so what I also want you to do I want you to give as much context as we can for now. Tell it real quick. Google sheets open up Google sheet you can have this open on one window and then have Google sheets open on another and I want you to kind of explain just briefly when it comes to what is shown on the tenant payment checklist.

Okay.

And on the parts that are important. Oh, yup. So you can just literally go down each individual section and just speak. So basically when I do this, this is just a heads up.

Yes, yes, Phyllis.

What I usually do is that I lock it, I vent my thoughts, and then you could be on this screen, vent your thoughts, and before you end the conversation, make sure you go back to terminal, make sure your cursor blinkers on, and then end the conversation, and it'll paste everything right there.

Yes.

You get what I'm saying? So make sure you click, make sure you can go back to the other one, just kind of vent whatever you're looking at when it comes to Google Sheets, and then before you end the conversation, paste it there.

Okay.

Gotcha. Okay. Let me give you a quick test and then take it from there. So my Google Sheets in Google Drive, That one is called tenant payment checklist, And that's the exact sheet on the file that we're Looking forward.

Make sure you explain.

So they don't pay me checklists that way. We have a lot of properties in column A, that's the address. column D, I'm sorry, column B, that's the type. So basically, Whenever the tide is Rent to own. Those are usually due on the 25th of each month. The due date is represented on column R.

Exactly like that.

Got you.

So keep explaining it real fast. Do you understand that when you explain, I guess, yeah, just keep explaining it real fast. Keep explaining it.

That's perfect. Keep explaining it.

Oh, I didn't need to fix anything.

You don't have to worry about being grammatically correct. It understands what you're saying. And trust me, I'm trying to tell you so easy. Just go ahead and continue explaining it. But this time, don't stop. Explain as much as you can about it. how it functions, how it works, try to do this instead of just doing it like back and forth all over the place.

guys.

Try to save time, just go right in a line. Just what every single thing does, every column, and it does.

Okay.

So, when you start on column B, don't just say, oh, when it's seller finance, it does this. No, just say that these right here are all the different type of deal types. Just tell it what it's doing column by column. -Of course, of course.

Okay, I mean, I just wanted to test it first, to be honest with you.

Usually I click on control and the Windows button. That's how I get Whisper up.

No, for me, I changed mine to controlling zero.

How do you lock it? What do you click on?

So instead of it being like right close to each other, I have to use both hands, it makes it a little quicker.

Oh, okay.

So So just again, you can start off anywhere you want.

Got it. Okay.

All right. Yeah.

Go ahead and start off with column B, explaining each one of the places. Yeah, let's do it.

Okay.

So on the other hand, for whatever the yield time, If it's different from rent to own, usually that's due on the first of each month.

We have the tenant payment amount that they should pay in column N.

OK.

Let me try this. Pause it, Professor.

Or paste what you have.

Hold on, hold on, pause for a second.

That's what they should pay on a monthly basis. have three check boxes, In columns O, P, and Q, O is payment processing.

Hold up, hold up, pause, pause, pause. Can you hear me? Pause.

Peace. Here. Q, that's the indication that this specific property is Section 8 About 80% of those tenants. So the tenant's nickname inside that address or property. they are represented in column D, the phone number in column E, and also if we have a second tenant or a relative, His name or her name is in column F and the phone number is in column G. Usually, about 85% of those tenants made their payment on door-to-door.

where the status of a payment on door loop goes into pending or processing, Only by that time, we would Check the checkbox In column O, for payment processing and accordingly based on the script in place. In the automation, the role will light up in yellow. Once the payment on their loop shows as processed, Only by that time, we would check the checkbox in P representing payment clear And that's when the road goes into green.

Okay, so you have to make sure, did you hear me?

So you have to make sure that before you stop it, you have to come back. and click on it. So now what you have to do is that you need to go to, no, no, no, and then delete, and then delete, and then delete.

No.

You gotta open up WhisperFlow and then copy it there. Just open up WhisperFlow. Oh, that's it.

Oh, okay. Oh my God. It's like, Oh. Okay.

and copy. That's fine.

That's crazy, man. Oh, basically.

That's fine, it's copied. But this is, what I was saying was this, was to go through each one line by line. Do you want me to go ahead and explain it real fast? Just to be a little more thorough? Because there's a couple things I noticed that we didn't copy, we didn't, I'm just going to do this. I'm going to explain. I'm going to re-explain what you just said. I want you to stay. I want you to keep.

I want you. I want to look at your screen.

Okay.

I'm going to put it in the chat. Or actually I'm gonna put it on Telegram so, 'cause I'm not sure if the chat can It won't copy everything over. Yes.

Take care.

Okay.

Okay, cool. I'm gonna stop her. Yup.

I'm literally going to do it step by step because that's all I was saying to go. Column by column, you're kind of jumping a little bit. I'm gonna just go column by column, explain what it is. And when I go over the columns that have deal type and occupancy, I want you to click on them so I can see, I can read all of them.

But I want to listen to you, how are you going to do this, like the same thing I did, but in your way so that I would know how to.

Okay, yeah.

Okay.

Okay? No, when I say click on them, I mean like click on the actual dropdown so I can see what the options are.

Oh, okay, gotcha.

All right, perfect, here we go.

Okay, so The file itself is called Property Payment Checklist and where we keep up with the tenant's exact payments is under the tab called Tenant Payment Checklist. So for column A is what we have as the address. Column B is called the deal type. And the deal types that we have is called rent to own, seller finance, normal rental and section eight. Section C is the occupancy status. The different statuses we have is called occupied and vacant.

column D is called tenant tenant name this is the first and last name of the tenant or at least the primary occupant Hello, hello?

Did it record anything?

Ah, damn it. It didn't record anything. Hold on. Is there something?

Now it was basically saying it didn't know which microneed. Let's do that one more time just really quick.

All right, I'll do it fast.

okay so the prop so where we go ahead and we check everything out is called the property payment checklist and the tab that we work within is called tenant payment checklist column a is what we have as the address column B is the deal type the type of deal types that we have are called seller finance rents all normal rental in section 8 Section C is for occupancy status. The different statuses we have is called occupied or vacant.

Then column D is for our tenant name. The column D is usually for the primary tenant that we're in contact with. And then column E is occupant one phone. So it's usually the phone number that's associated with that person who's in the house. And then column F is for tenant name two. So those are usually the spouse or someone else that we're going to be reaching out to as well. And then in column, so that's our first and last name. And then column G is their phone number.

Column H is if there is a section 8 and the government percentage. So basically that just means that the percentage that the government is handling and the way that you'll know whether or not that's a section 8 is from the deal type. then column I is the amount that the government is actually paying of that person's rent so that's instead represented by a phone number by a dollar amount that the government is paying and then column J is section 8 personal percentage responsibilities so this is just the percentage that the person who's living the house is personally responsible for And then column K is the personal responsible amount.

So that's basically the dollar amount that they're responsible for. And then column L is the tenant payment amount. So, this is the amount that the tenant is actually responsible for and that they're paying in full. And then column M. Mary is the section 8 HUD payment. So again, this is a reiterating of what the government is actually going to be paying column end is the total So this is just going to total how much the tenants responsible for and how much the you know The government's responsible for if that's applicable, but this is just the total total one thing that I did want to mention was that when it comes to seller finance that The way that we track those payments is through our servicing company.

or if we're handling the payments personally. so but It just depends, but it's on a case to case basis when it comes to the seller financing. But when it comes to rent to own and normal rentals, as well as our section eights, all of those payments are being tracked through. Door Loop. One thing I did want to include is that the payments that we received back from the government is actually going directly into our bank account, which is called Base Lane.

and the payment that the tenant is responsible for is recorded through door loop. The next section that we have is column O, which is called payment processing. And that's represented by a check mark. Essentially how it works is that once we see that the payment is actually processing, so usually this is, we can make it real simple, this is meaning that if we're on actual door loop, And the payment is shown.

No fucking way. I think it's not recording. I'm about to freaking flip.

No way.

Not even in Whisper?

You know what? No fucking way. That's nice. This thing stopped and I didn't see it.

The same way...

This is still.

What the fuck is going on?

Okay, this is ridiculous. Okay, we still need to explain this thing. So that's the biggest thing.

I can do it.

So, um, God. Damn it, we need to explain it. Um, okay. Okay, go ahead, please. Okay.

Let me jump in. I mean, you tried to help me, so...

Love you. Thank you. Please go ahead. Please, Jesus.

Yeah. Okay. What?

Go ahead, go ahead. Start off with, Started with column D because I think that's probably the only part.

H.

Start up with actually not column D, column of... Start off with column H.

Yeah, yeah, that's true.

All right. Yeah, H, Section 8 percentage. You never explain the Section 8. and also I think you also need to include the type of so the property payment checklist you did you made it where it seemed like the name of the entire file was called tenant payment checklist you have to make sure you're specific so it knows where to check for things so you have to make sure the file name is called property in the checklist and the tab is the other way And that's it.

Okay.

Just start off with the title and then go into column H, I think. So we're good. Go ahead and continue.

Okay, I can't do it to fix it from here or just say Okay.

Great.

Listen, listen. This is what I'm saying. You can be sporadic. You can be all over the place and still understand what you're saying. It's going to compute everything that we say. It don't have to be in order. So let's stay on track. So just start this recording.

Okay, so just rehearsing on what I mentioned before. This treat It's called the tenant payment checklist. However, the whole file is Property payment checklist. So inside this tenant payment checklist sheet, Uh, For column H, That's showing the Section 8 or the government percentage. That's the percentage of contribution from the government towards part of the rental, for this specific property In column I, that's the amount which is represented by the percentage in column H.

In column D, That's the the percentage of the amount that the tenant inside that property which is under Section 8, would be paying In column K, that's the actual amount represented by that percentage in column J. In column L, that's the tenant payment amount which is the actual total amount that tenant P by himself In column M, That's the amount, again, being paid by the government which is called Section 8 Hype Payment In column N, that's the total amount required for each property every month.

Also, just to rehearse, Yeah. properties or the deal types that we have in place Our rent to own Seller Finance, Normal Rental, And section eight. In column C, that's the Occupancy status, And we have two of those, either occupied or vacant.

Peace.

Perfect. Okay. Go ahead and also explain where it can check. for payments like door loops,Uh, And as well, so door loop is for rent to own, section 8, and normal rent sold.

Okay.

And then when it comes to seller finance, we usually have those amounts serviced. But it's on a case to case basis. Sometimes they do go through door loops, sometimes they don't. It just needs to be identified. Um, And then when it comes to The Section 8 specifically, we received Section 8. The government side is paid directly into our account and then the responsibility, the part that the tenant is responsible for that we actually determine if it's processed and cleared is based off of what they're responsible for and which is shown on DoorLoop.

Can we build a skill first based on the door loop part and then we can expand it to the other ways that we get paid from?

It will probably be injustice because I can understand if I didn't know it, if we didn't know how to explain it, but we can explain it right now.

Here you go.

So we can still be able to, it's not that hard. It's really not that hard, I promise. So just explain it like I was talking about so I can make sure it has full context.

Okay.

Because what we don't want to happen is that we don't want to have to explain that later. So go ahead and go back real fast.

How about Terry?

Thank you.

Yeah, perfect. No, right, where we see payment processing. So, explain to it, right, where it where we can be able to track the payments for each one of those seller financing Or I can retry one more time and let you take it over from there.

Okay.

Okay. Just bear in mind that most of them are dual loop. Only for this one here, 4438 Puffer Street, that's on one-point lending. And Okay, what I'm trying to say is that not all seller finance are the same.

We want to keep it general and by saying just on a servicing company, and then we can identify that part later.

Yes.

You know what I mean? Okay.

So that's where I'm saying that we can let-that's why I kept it general. Let me explain it. and then I'll put in the chat. And then I guess we continue from there.

Okay. Okay.

I promise we're going to get this working. But I'm only going to explain that one part and then you'll continue because I know you know the rest of it. Test, test, test. Okay, and if you don't work, I'm throwing you away. Okay. Here we go. I'm going to keep making sure I can see that my voice is still moving. Okay, so next is how do we actually check to see if payments are made? So for seller financing, We usually have those payments serviced. That means that we use what we call a third party servicing company.

However, it just depends on the deal. Some of our servicing, some of our seller financing are handled through a third party servicing company. Some of our seller finances are still on door loop And some are Actually, right now they're either on door loop or they're handled through a third party servicing company. That's just to keep that part of mind and depends on property to property. However, for rent to own, every single one of those properties are shown through door loop.

when it comes to knowing whether or not they made the payment or not. And when it comes to the rentals, normal rentals, those also are recorded on door loop. And then when it comes to the Section 8 tenants, The government's part, they make their payments on the first of every single month and those go directly into our bank account. But what we track is the seller's percentage, their part. So the part that they're responsible for, we can be able to see and track that through DoorLoop as well.

Go ahead and insert that into there. Let's go.

I can't wait.

You're going to see here in a little bit what this does. It's going to be amazing. Go ahead and continue. This is why I'm like, let's build it together and then we're going to see.

Okay. You got it.

All right, go ahead. Have we, I don't know, I don't think we explained, no, we ended it off on payment processing.

Okay, so we are good with those here, those three ones. Uh.

Oh, I did.

We never went, we didn't, it didn't record my voice.

Oh, you did? Okay, okay. Uh, And I don't remember you talking about the HUD payment cleared.

I did. Oh, thank you. Yeah, yeah, yeah.

I did. Look at that.

You-no, no. We-we don't-we-yeah, go-we stopped that. I know we stopped at right before then.

Okay, that's fine.

It's here, it said those ones. But I mean, if I rehearse on it again, that's not a big deal, right? Okay. Okay.

Okay, so just as a recap, I've got him.

: O, P, and Q. in order as payment processing payment cleared and then section eight That's the HUD payment cleared. checkbox. So for those three columns, They have check boxes and simply we check box for payment processing, only if we see the payment showing as processing on DuraLoop or On the third servicing party, Hold on. After that, we check the payment checkbox, "Payment cleared" in column P, only if the payment is showing as processed or completed.

for Column Q, which is representing the Section 8 HUD Payment Clear checkbox. This one here. We check it. When we receive the payment from the government, which is being paid on the first of each month into our bank account, directlyWhen old boxes are unchecked Okay.

You don't have to worry about the color.

Column R.

So remember this, you don't have to worry about explaining colors to it. It doesn't need to know the colors. You just need to explain these columns. That's it.

Oh. Okay. Got it. Okay. That's fine.

Uh, So where are we now? Yes, due date and then grace period.

Okay.

We're on column R.

Trust me when I say it's smart, it's going to figure it out. You just got to explain. That's why I'm like it's simpler than what you're explaining it.

Just go through each one and explain what it is. Continue.

Got it, okay.

Now comes column R. That's the Dulee. It's very simple. So for Seller finance, that's usually... do on the first For normal rental, that's on the first as well, Rental owns are due on the 25th And Section 8, that's due on the first of each month.

Okay.

I'm sorry, Josh.

No, no, no. You probably should have even some... I know I'm micromanaging. I need to stop. So, no... Keeping it even simpler, you should have just said due date. So the thing is, here's the thing to keep in mind. If you tell it, well, you know what? You say exactly how you think. Go all the way through and we'll finish it up. I was just thinking, again, this is just how my brain works. I'm thinking beyond it.

I just know that if you go ahead and you say something like that, of saying that, oh, on the 1st, seller finances are due, on the 25th, it's due on this month.

This one.

That means that if there is an outlier, like for instance, rent to own. We do have a rent to own right now that's due on the 1st.

So rather than just saying that that's the due date, you went ahead and you collaborated with, oh, seller finance doing this stuff. Now, when we do seller financing, it might actually remember that and say, oh, OK, rent to own. That's on the 25th. But let's say we had a scenario like Lipscomb.

um Okay.

right where their payment their rents own but their payments doing the first it's going to measure with that that's why I just keep it simple just say due date these are the due dates grace period grace period late status that's where it shows these behind just like that You can just delete the previous one.

So how can I cancel this last part?

Oh, do you mean each property or each column? H-Com, okay. Like, generally speaking. Okay, got it. Oh.

But I would just go through each one very quickly.

This one.

This part is kind of easy.

Beach collar.

Just keep it simple.

I think it's the Oh.

That one, yeah, that's perfect. That's perfect. That's it.

That's it? Okay, cool. Wow. You got to be cautious with that. Okay.

So for comr-duty, Bum S, that's the grace period. which is counted starting the Do you need? and after it finishes, That's when This tenant is considered late CUNYMT, that's late status, you... days behind and that's a count. This column is numerical. every time it reaches the end of the month, it would throw an extra count of one so that it would add plus one to the adjacent cell in column V that's representing months behind.

Once that one is added, The cell in column U is reset to zero.

It knows how to do one.

W. this upcoming or past due date Column X is represented by drop down menu for note being serviced this other yes or no if we have this note for this property being serviced by a third-party servicing company Call them why. Is this a private money lender? Yes or no. That's a checkbox. Column Z, that is the property manager amount that's a dollar amount Colin EE. that's the property manager percentage of The income of this propertyProblem AB.

How much she's getting paid?

That's the borrower's payment last made and that's date format.

Don't skip it.

Keep going. Don't skip nothing, please.

Yes, sorry, what was that?

Oh, you're pacing it. Okay. No, no, you're fine. I was, uh, so I was still... Explain the rest of it. You're almost done. Yes, every single thing, all the way through.

Explain what? Like those ones as well? Oh.

Every single line, we don't wanna skip it 'cause whatever, like, so borrowers payment last made.

This is the thing, it can actually help us build this. So it finish some things out and complete some of the things out. We want to explain every single line to it. So if we needed to log into somewhere, it knows where to go. It needs to explain, understand the entire thing.

What about those ones here?

In transit, yes, everything. Yeah. Oh, do you not know what they mean? Oh, got it.

No, sir.

Okay, so go back to where we were just last at AB. so a B is the borrower's last payment so that's the payment that's the last time that the the the borrowers have made a payment On that, we can, looking at the dates right there, we don't look like we have that automation all the way filled out yet. So, We just put that in there and just say borrowers last payment made.

Transit ETA.

Yes.

It just means how long does it usually take for us to receive that payment in our bank account. Arrival deposit ETA is just how long do we expect for it to actually arrive, until it arrives in our bank account.

Okay.

Overall account late status, is it current or is it late?

Okay, and this one as well.

Technically, we don't need that stat. We only need that. Yeah, we can delete that whole thing. Current reset, yeah we can delete that one too.

and then boom all right you got it let's go ahead knock it out let's knock it out let's make it quick we're gonna do this real fast Which one?

Got it.

Also, I would actually take those here off because we have them right here. This one, those more distinct ones. We have the money satis-seed complete. We didn't need them. Yeah. And you know what?

Okay. Okay. Okay, that's fine with me. Go ahead.

I'm sorry. Sorry. And this as well. We have those here inside the loan status sheet.

Got it. Okay, let's go ahead and delete those then.

Okay.

Column AC. That's for transit ETA That's representing, that's a numerical representation Twitter? And that numerical figure is simply representing how many days needs so that the payment would reach us from either the third party servicing, Company or Duraloop. Column AD, that's a date format. for arrival deposit eta Dance. the approximate date when we are expecting that amount or that payment from Duraloop or the third party servicing company to hit our bank account in Bay's Lane, AE, that's the hyperlink.

for the tenant website or portal, AF, that's the username. AZ, that's the password.

Good job.

Okay.

Um, Okay.

So one thing I want you to add today is that we also need to make sure that you have access to Google Sheet and Door Loop. Just add that in. We also need to make sure you have access to Google Sheet and Doorloop.

Wow.

Okay. Should I give it the link to the Google Sheet?

No, that's not how we connect it.

We need to make sure that you have access to Google Sheets.

It's through MCP. So just say we need to make sure you have access to the Google Sheet in Doorloop.

Boom!

and do a loop.

Okay, it makes sense. Yeah, there you go.

Okay.

Wow.

D-O-R. Okay, enter.

Okay. Enter. Okay.

Just answer.

It's going to be heavy. Do I need to take a copy first or something? Or you're good?

I'm very nervous.

Now it's going to read through all of this, and now it's going to ask some clarifying questions. so he can make sure he understands everything.

Okay. Oh, great.

That's what I'm saying. It's not gonna just build it. It's gonna read through it. And then it's going to tell you what it thinks. So it's going to need to be built.

I can see me.

Given the excellent context of the sheet structure, I have rounds one and four mostly covered. Let me ask a few focus questions to nail down what the skills should actually do. Okay, here we go. So it says right here, what should a skill actually do when invoked? Pick all that apply. Check door loop and update sheet. Pull payment status from door loop automatically check and uncheck OPQ question check boxes in the Google sheet.

Yeah, sure um read the sheet state and procedure, I produce a summary of who has paid, who is late, who's pending, which is right up here, which says no. Flag overdue at risk tenant Send reminders or notifications, emails and messages to tenants who haven't paid. See, yeah, we can do that. Okay, I kind of have an answer for that one.

Go back to the sheet for me.

So I guess there's a few things that I wanted to be able to do. Go to the left. Let's keep going to the left.

Um, Let me see how can I... When I raise my hand like that That means that I want you to go ahead and move to the right.

Okay.

So, I'll have to stop talking. Okay.

Oh my God. You see this here? Those ones? He picked my... Pick my piece.

Thank you. Yep. What? Your voice. Okay, just go back. Just expand it so we can see what it says.

Okay.

I think...

Expand it. Okay, just go ahead and click that.

Yeah, it picked my voice. Here it is. I'm going to delete it, but I want to make sure that there's no...

I wouldn't delete it.

I would just go back like I was talking about. Just click back.

Like undo?

Yeah, I'm doing it. There you go. Just keep going back until he's not there anymore. I think we're good. Perfect. Okay, perfect.

Period.

So let go ahead and start to the far left, please.

Oh, you're doing those? Okay, perfect. Go ahead and start to the far left. Alright.

So what we will want This to update is...

What happened?

I said, move to the right. So just bring up the mini thing so you could be able to see me. So I was saying I'm gonna raise my hand it means move to the right Oh, I mean, I don't know.

Where are you? Oh, here you are. What is it? There it is.

That's crazy, man.

Okay, cool. Let's see here.

Okay. Okay. Visit again.

Go ahead and start off to the right a little bit further. Right where it gets those checkboxes. All right, perfect.

Okay.

So just so we're clear, I'm going to cover O, P, and Q.

And then move to the right, and then move to the right, please. No being serviced.

He moved into the right. Please.

okay A, B. and A, D.

So A, B, and A, D. Oh, take off A, E, and A, F, please. He goes off. Perfecto. All right, let's go. Let's do it. Go back to, there you go. Perfect. I'm going to start it.

Okay, so what we will like you to be able to keep track of is O, P, and Q. So the payment processing, basically that's something that you could be able to see whenever it is through door loop, you can see that a payment is processing. Payment cleared that just basically means that the payments have actually hit inside of our bank account and actually cleared Um, Also, Q for Section 8 payment cleared as well.

And then for the A, B. borrowers last made payment so once the payment has cleared you will reflect your that amount or that date that it actually officially cleared. on the the correspondingRole? on column AB. then you will on that same date you will also put in the ad which is the arrival deposit ETA so basically you'll just go ahead and do a quick math of A. B. plus AC and then AD. Honestly, you can probably just go ahead and create a formula.

that can be able to auto populate those so that as soon as you make the payment cleared it will automatically Find the date in AB. and do the math for AC to equal AD.

Go ahead and copy all that and put that in the last row.

Starting here.

Right in here? always a button.

Okay, so how do I...

Yeah.

you Got it.

So go ahead and move your cursor.

There you go. And then paste. Control V. There you go. Enter. Enter.

Is it not clicking?

Enter? Okay. So is it not...

So when I click enter, it checks it.

Oh, yeah, I got it.

Answer it.

Okay, perfect. Um... Let's see.

How often would you invoke this skill and who triggers it?

Manually a few times a month, daily to keep the sheet on demand when scheduled, automated. Set it automatically on a Chrome schedule without doing anything. Okay, go ahead and go to the last section.

Okay.

I want you to use Claude's schedule. to keep an eye on this daily. That's it.

and basically what I want you to say is that I want you to use Claude schedule In order to look at this daily, I want you to use Claude's schedule in order to set this up daily. Let's change from keep an eye on this daily to trigger this daily.

That's perfect.

I mean, it should be smart enough to...

No.

Look into it only if we have something pending or we need a payment. If all is green, it doesn't need to trigger.

No, just click enter.

Just click enter. Perfect.

I'm sorry? Oh.

Okay, door loop. For door loop integration, how do you currently access how do you currently access Dorothy and Dorothy?

It's manual.

Okay.

Just go ahead and let me go ahead and give this to it. No, no. You gotta be smarter than that.

You gotta be smarter than that.

Because the way that it communicates is through CLIs as well as MCP integrations. So we don't want it to use a login because that's going to make it go slow. We wanted to go ahead and be a part of his back office. So let me go ahead and...

Okay.

Not yet.

So which one do you recommend, like the API?

Okay.

No, I want to give this to it. Well, it's probably going to be API, but we're going to give it... To save on time, of course. Yep.

So just send me a text message.

Wow, I love that.

But I think the biggest thing brother is keeping it simple.

It's different, man. Yeah. I noticed.

It's really keeping it simple. Like you gotta just be very fluid. with their answers and not to overthink it. If you overthink it, if you get too analytical, it's just going to take you down a rabbit hole.

Mm-hmm.

That's great.

as broad as we can. All right, cool. I'm going to give this... It's just literally just copy paste, copy paste.

Yes.

There you go.

Okay.

Last one?

But these really don't, these don't take that long. So just say that here's the API key for door loop. And the last one, very last one. Here's the API key for door loop and then paste.

Okay.

So in the inner so what I want to tell you so yeah, and it's gonna review everything and then submit answers click enter So one thing I want to tell you, so it's thinking right now.

Here is the API key for door loop.

So while it's doing that, one thing I want to tell you is that everything is very, very conversational.

Yeah.

That's how it's able to read everything just like you know, right? So there is no straight structure way to do it when it comes to how we integrate. But what we can foresee is that the more deliberate we are in being specific, the better it actually can be able to help us. So the less things, yes, it can interpret a whole lot. But if you can just be very specific up front, it will... It will need to interpret less.

So yes, but if you just make everything super broad, then it's just, it's going to make the skill. Now, the thing is, here's a good thing about it. it's going to ask you enough questions where it's going to get specific. But here's the thing though, Because we were very specific in the beginning, can you imagine it's going to ask us enough questions to get all that information anyway. But how long would that have taken?

yeah.

Oh my God. That's why you said explain.

It would have taken a long time. long time. That's why I'm like just be specific up front.

That's why.

Everything. It says it already went through one through four of understanding what we're looking at. Okay, here we go. How should the skill match a role in the Google Sheet to a tenant record in DoorLoop? The property address. So, multiple. So, it would be like I would say the property address, tenant name.

That's the ad-lib.

And, um, Let's see here. Well, one thing we could probably do that can help it out a little bit, we can actually create a section. called Doorloop ID. Yeah. Let's go ahead. Let me go and open that up real fast. I'm opening up. Actually, you have it open right now. right yeah go to probably paying a checklist real fast go to the far right right side and then on the just add a new road to the right and call that door loop ID Just call it door loop ID.

Perfect. A-H. Okay. Perfect. So, we're going to go ahead and say this.

So the way that it will be able to track Which tenant is which is through The address, the tenants name, The phone number. as well as door loop ID. Now what we did was that we added an additional column called AH where You can be able to input the door loop ID once you find it. And what this will allow is that in the future, you can be able to quickly identify that person through that door loop ID.

But that would just be a one time thing where you got the door loop ID and then it will go ahead and work out that way. So what we can say is, For every new person that is added into The system That. And once that person is found on Door Loop, you automatically be created with a door loop ID So those are the different ways that you can be able to find the personal door loop.

All right, just put that inside the chat. 202.

That's good.

And then choose this one here, number five, right?

Just choose number five.

What's that one more time?

Yup.

Give me a quick second. I'm gonna give you the sheet access 'cause that's a little bit longer, but I got you.

Okay.

It says here already authenticated.

Let's see here. I might give it my Google Access.

Yeah.

Oh, MCP, Google Drive. Oh, there it has it.

I already gave it to it before.

All right, perfect. Go ahead and click that one. Answer, please. Sinead.

Yes, sir.

Oh, I love that. This is beyond.

Okay, so let's see here.

Trigger scroll up just a tiny bit. Let's read that real fast.

Okay, good. Here's full summary understanding. Run daily to sync door loop payment statements into tenant payment checklist sheet and auto calculate arrival deposit dates. Runs on a daily schedule via schedule can also manually invoke to when tenant payment optional a specific address or door loop ID to process just row instead of all rows okay Process head all roles to.

Okay.

Skip rows where column C is vacant. Okay.

Um.

Okay, for each occupy row, look up the lease and tenant in door loop using the door loop ID column, yup, or fall back to the address and tenant name.

Pull payment status from DoorLoop API, update column O payment processing if status equals pending and processing.

update column P payment cleared if statuses process is completed When P is checked, write the clear date to column AB, then calculate AB equals AB plus C.

Mm.

Okay.

Update column Q, section 8.

clear for section 8 properties when government payment is confirmed on the first on the first.

Log off.

changes made in that run and puts Google Sheet, okay, dependencies.

Guardrails, one thing to confirm, you mentioned column H for door loop ID, but earlier H was described as section 8, government percentage.

Anything.

What?

Possibly shifting.

okay so does that capture it No, it's A.

So it's column A-H.

Yeah.

Yeah, that's what you want to add at the bottom.

How can I do that?

So just, just.

Clear up the confusion that it had in common language.

Just explain to it like it's a person.

Oh, you mean like that? Yeah, so just go ahead right there.

so control zero explain it just like a normal person who just explained this back to you how would you talk to them yeah exactly Okay.

Okay.

Just a simple correction for door loop ID. It's column A H. A for Alpha, H for Harry.

I mean, just let's take this off.

Okay.

That's funny.

Okay, excellent. Listen.

I'm happy with that. Did you? You want to add anything?

Yes. One gap that I don't think is seen yet So Is that It's the What was it? It's the, um... And something we need to add to the skill builder is, well, it needs to test to make sure to see if there's any gaps anymore. Um So, but one thing that I saw as a possible gap Um, going to be checking for Yeah, section 8 payment.

Section 8 payment.

obviously That's what I had in mind.

Yeah.

Yeah, so I think it needs to notify you. So I think it just needs a process. It needs to create a process in which it will contact you to get your response back for Section 8 payment, and that's pretty much it for now.

until it has until it has Bank access. Okay, so here we go. Give me a second. I'm going to say this and then...

I'm okay.

Okay, so one small gap that we saw was when it came to the Section 8 cleared. So you won't have access to the bank in order to see whether or not we've received that payment or not.

But what we would want you to do is that there should be a way that you can be able to request that information from our associate Mustafa that's mo s T a FA and from there from his response You can be able to update That area.

I'm not exactly sure how you're going to fill in that gap.

Bye.

Go ahead and solve that with an idea that he can use in order to inform you.

Also, We want you to go ahead and go through the system to see whether or not there's any gaps that you see as well. Well, the whole thing is to have it where it is.

Actually, Josh, I see that I can just Check that checkbox.

Men.

It's only one.

The whole thing is to have it where it's easier for you. So it's gonna come up with an idea Crazy, right?

Okay.

You got it. I mean, Unbelievable. Unbelievable. It's homeless.

Yeah.

And like I said, I want us to go crazy with adding skills. So every, this is where you, the way that you think about it, it's like, what don't you want to do every day? But you have to be specific enough Yeah.

I could be very precise as you just did now and very accurate, But I mean, I can do it.

It's very simple. I'm just a little bit nervous, you know?

What? It's called delegating.

as if I'm having What?

It's called delegating. It's like me with you, right? Some people are nervous about hiring somebody to help them because they don't want them to make a mistake. You don't want them to make a mistake. And so did you make plenty of mistakes? Was it, did it take a long time and does it still sometimes take a process to train you? But yes, but is it worth its weight in gold once you figure it out?

Okay.

Absolutely.

Yeah, you're right.

It's the same thing.

Of course, 100%.

but obviously way more powerful.

But obviously this right here, this skill that I'm giving to you is infinitely more, this is beyond efficient for me.

This is, you know what?

This is a magic wand.

-Literally, this is the craziest thing about this.

Seriously.

You working on this, creating skills, this is where I want you to change your mindset. This is you working.

You creating skills to get things done, Is you getting things done? There's people a thing that I realized her who's one of the people like the person essential YouTube is He said that he spends his entire day in cloud coat.

Yes.

And he's able to learn, like he's able to get more things done than 99% of the people in his industry.

Thank you. Let me give you a very small example.

And he lives in Claude Cull. He's getting work done. So it's not you not working.

For example, if I had a task to check on the payment status for 10 of those tenants, okay? This, I mean, deep in details, if this could take me like an hour, But on the other hand, But on the other hand, if I spent that hour investing that hour in this here This would do the same task, which is checking the payment status for those 10, but it's not going to be for once.

And Go back to, while you're talking, go ahead and go back to the things and make sure it's not stopped.

Okay, keep going.

It's going to be for... For good. Yes. So spending that one hour investment here is worth, I mean, there's no even comparison.

Yep.

Yeah. Every day.

on their outcome value.

Yep.

your task is to first check to make sure that this is working right. And that's the biggest part, just making sure that all this is working. And then to add to that skill. So you can actually add to the skill that says, hey, I want to edit this specific skill.

Yep.

or expound on it or change it or whatnot.

So one thing I don't want you to do, this is just between you and I. What I don't want you to do is that I don't want you to end up going through a whole bunch of videos and do what a lot of people do, which is that they just add random skills Whole bunch of skills, 'cause there's skills that you could add in for the internet, Do not do that at all. Most first thing Security risk.

Of course.

Yes. Got you. Got you.

Okay. Well, this would take me to a very important question. How much did this cost from Pray to men.

There's a lot of people out there who are putting out information to have it where there's the skills are grabbing personal information and sending it somewhere, right? So that's one. And then two, relevance. A lot of times the skills that we're adding in there, they're not even relevant. And too many skills can clog up the efficiency of our bots in the long term. Because now it might have conflict information, but you personally added to the skill is always going to be relevant.

Yeah.

It's way cheaper. It's still the hundred and something dollars a month. 130.

compared to me spending more Like, yeah, it's still within the same subscription tier.

of 130 compared to almost a thousand.

All of this Okay. Okay.

I just, I, I, I, I, already reduced my subscription tier back down to $30 a month so that Yeah, I can definitely see myself just canceling it at this point because I can add a skill for it to do research.

This one?

Go ahead and full screen this so we can be able to end this off.

Go ahead and full screen the bottom part, the visualizer.

Yeah, the bottom.

Yes, sir.

Okay, cool. Let's see if your gaps I'm solving section eight.

Okay.

skill sends an email to Mustafa on the first listing all unchecked section 8 properties he replies all confirmed actually you know what let's do on telegram Let's have it reply to you on Telegram.

oh 40, yeah, okay.

Okay. Of course.

You're gonna go ahead and tell it. Okay, let's keep going. Missing door loop IDs, column A-H is empty. Skill auto searches door loop for addresses. If found, writes ID A-H. If not, flags and run log. Okay, third party servicing roles, X-YES. Door loop may not be the source of truth.

Skill logs a warning and skips auto checking without a confirmed door loop entry.

Okay. Oh, got it. Third-party servicing.

Okay, got you.

So it says for now it's going to skip it until we go ahead and train it on how to actually do that part. But remind you, once we want to expound on it, we're going to update that current skill.

Okay, so column W.

Upcoming and past due date.

skill auto populates upcoming duty if unpaid past you if beyond grace period next column W upcoming past you was column W show me column W Upcoming is not is that auto is isn't that one formula?

Excuse me.

Uh.

That's a formula.

We shouldn't change that. That's a formula. That's auto-generated. Yeah, we don't want to change that. Yeah. Go back, please. So that's why we're going to read through everything. You can't just...

Okay, cool. So yeah, we don't want to do that. That's a formula.

Skill auto populates, no don't auto populate, nothing. late tracking TUV skill auto increments late days I had to roll over, that's fine.

AD desk that's fine okay so this is where let's see here okay so section eight four four replies For column one, I want it to reach out to you on Telegram. And then for gaps one and four is what we're changing. So in row four, or gap four, column W we need to tell it not to do anything to column W since that is auto POC that's a that's a that's a formula No, skill autopop is upcoming.

That's what it says here.

It says skill auto populates.

Okay.

No, skill autopop. That means itself. Just to make sure we're clear. The way I read it is that it's going to auto-populate. Just make sure we confirm. Okay, just do 1 and 4 like I was talking about.

Okay.

Telegram and just skip the comma W.

It says yes and allow. So this is what you'll do. Basically, see, so yes, we want to create the skill but click tab, this is how we can add to that yes.

Tab, okay.

yeah perfect and then go ahead say but Tell it that you want it to reach out to you on Telegram and then tell it to skip column W since that's a formula.

Just speak though, speak, speak, speak.

Okay.

Yes, I can.

I would rather prefer if you reach out to me on Telegram instead of sending me an email. Okay, and the other point was for column W, Just not to touch it, right?

Four.

Column, yeah, gap four and for column W don't.

Don't touch it yet because that's a formula.

You don't need to touch column W because that's a formula. and the date in that column, populates automatically. Okay.

That's it.

Go ahead and enter.

Okay, anything else? See it?

And then full screen that one more time. I'll go ahead and full screen that for me.

Wow. I love that. Seriously. Sorry, what was that? Oh, close screen.

Full screen. Perfect.

It's working, but it's stinking.

Perfect. Give me a quick second.

Okay.

Okay.

What did you click? I'm not sure why you're there. Full screen?

Hello.

Something public.

That's fine.

Full screen? Okay, let's see, two clear updates recorded. Swap email for Telegram for section eight.

Yeah.

Let's see. Update SQL Tracker, open changes in visual code. Yes.

What do you mean?

Let's keep it on email, Josh. to make it, I mean, Yes, Constie, and yes, people.

It's not costing. No, I'm saying on Telegram you can literally be able to see that quicker than email.

Okay. I'll be honest with you.

Okay, we can have it be bold, but I wanted to have it where it's easy for you.

I'm on top of my email. If I get a notification, I just put it in right away. Okay.

I don't want to have it where you, like I want to have it where if you're just out and about on your phone, don't just blink right there oh did we do that okay i can check real fast Yeah. Okay, let's see.

I want to make... Open changes in Visual Studio, put a tab, and then just say, Yes, however, do you have my telegram as well as my email that you'll be sending? Remember your voice.

Do you want me to ask it or give it something?

I don't know. Okay.

It says, but...

You can give it your Telegram number. And then And just, okay, we'll need a bot token plus your chat ID. Okay. So just tell it that, hey, Let's see what it-hit your bot token.

See you ahead.

Chat ID. Let me see.

I'm trying to find my chat ID.

You just click on the profile.

On Telegram.

Serenies. And Here it is.

I'm going to Thanks.

So... This So I am trying to send someone over my chat ID from Telegram. How can I find this? Your profile, your child, your age. Oh.

um I have it.

Okay. Go to Telegram again. Oh, you have it?

I have it as a QR code.

We shouldn't be, no. Go ahead and do this.

Okay.

Oh So it says reply back to, send this right here. On Telegram, I just sent you in the chat.

Okay.

So go ahead and copy that real fast. Go ahead and go to Telegram.

Okay.

And then go to--You want to go to Telegram?

Yeah.

And it's saying to...

Okay.

Apply.

Cool. That's what I'm trying to figure out. Who do we send this to? He handles.

Talking about, I'm talking about Telegram. for the chat ID.

Okay, so it says you send it to yourself. Send that message to yourself, please. How do you sound? How do you send a message to yourself?

you That's crazy.

I don't know.

I'm asking it.

Oh. Oh, it says go to the search bar. It says go to the search bar and paste that. Oh, oh, there it is. Okay, cool. And your chat ID.

Oh, I found it.

I did it. Okay.

So just go ahead and go back to it.

Okay, give me one second, 81XXXX1523, that's the one.

Please give your chat ID and then also give me your email and then tell it that you want the notifications to be sent to your email as well as your chat as well as your Telegram.

Okay.

So.

Just say it.

My Telegram chat ID is...

No, don't worry about that. You will need a bot token.

Okay, a bot token. Oh, working. We get the bot token. Okay, there we go. I got it. So it's at Botfather.

Do the same thing that you did with the other one.

And what is the But Oh.

The search bar.

But you have telegram open. You can literally just do that there. Yes. Yeah.

Writing a search, that's not a bot, yeah. That's not a... Brother. search In the second one, I think.

Oh, wait.

This one here?

Oh.

Yeah, try that one.

I can help create a telegram box. Uh, Oh, it says, okay, same process to start. and use new bot commandHi.

New blood.

Yeah, there's a new bot. I just put it in chat. Yeah, that one. All right, how can we call it? Please choose a name for your bot.

betweenConfirmations.

Call it something. No, call it section eight confirmation. Section 8 confirmation. Bye. Actually, no, what? No, no, no.

Let's do that. 'Cause what we'll do is that we'll make sure that No, let's not do that. Let's not do that. Let's do... Because... This one right here, we can do this one straight for rentals. So, um, we could do rental updates or something like that.

Bye. Go ahead.

Rental update, rental update.

That.

Yeah.

Yeah. do that.

And then, yeah, we have the S. Update bot, yeah there you go.

Update.

Good, now let's choose a username for your bot. It must end with bot.

Okay, same thing. Rental update bot.

Okay.

Okay, and then grab that API right there, please.

This one?

Yup. just grab the whole thing nope the whole thing there you go Copy that. and give that to it as well. Now also... Sorry.

Okay.

Oh, it hurt me? All right, come on. Let's go. We were taking a while. It's 2.30. Okay.

you and the Bunt Token.

is And also, I would love to have this by email as well.

We also want to give it your email because we also want that to be sent to you as well. and say, "And I will also want this to be sent to my email," and then give the email that you want to send to.

My email is Okay.

That's perfect.

Go ahead and enter.

Do you want to create-settings local JSON. I'll just say, sure, yes. I don't know how that works. Go ahead and say yes. Okay, let's full screen it one more time. Well, I guess it's showing you what it's doing in the background. Good night.

Okay.

I really didn't know that Telegram has A lot.

Okay. Oh yeah. You want to edit?

Do you want to make this edit to skill? Yes. Yes. And then, open the Let's see.

Okay.

Okay.

Yes. Yes, we're just yes all the way down until we see something there.

changes the Visual Studio.

I want to create a section, a confirmation template. Yes, why not?

Yeah, that's the one they're going to use to communicate with me on Telegram and email.

Like I said, I'm not looking at that.

My goodness, we have consumed 20,000 tokens so far since we started this session.

I'm thinking about how much it's worth to your department. This is at least an hour save for you.

I mean, Be I am. I am doing it.

Every time you do it So that was cool with me because it looks like I saved $7.

That's true. Yes, sir.

Well, I mean, again, we're there to make sure it works and make sure you understand it.

And also this is, like guaranteed outcome, no manual Like, you know what I mean?

So I won't say anything is guaranteed. I'm just going to check to make sure because I still can think of different ways. So the best way that when you think about this, you can't think about this as, you know, oh, it's guaranteed it's going to work every single time. We're there to check to make sure it does work.

So before we just leave it to autonomy, especially when you just create a skill, you don't want to go back to back to back to back to create skill, skill, skill, skill, skill. You want to create like daily and then check up on the previous ones to see if there's any updates that you need to do to them just in case.

Okay.

Like for instance, we want to have it where this tab is completely like checked in some type of way.

Okay. Okay. I mean, it's asking, do you want me to create memory? Why is it even asking me?

Just keep saying yes.

What?

Go ahead and set up the daily schedule.

Yeah, so Again, this is part of this is why I was telling you this is part of the.

Go ahead and set up the daily schedule.

theYield builder.

Do you want to proceed? Yes.

Yeah, sure.

So I was talking about the skill. Yes. Oh, it says yes. And don't ask me again. Yeah. So hold up.

So the next one.

I mean, that's what it's all.

I think there's a yes where it says don't ask me again.

It should be there. It's like yes to all, you know what I mean?

Yeah, they are, but...

I feel like I clicked the last yes.

I'm really happy to have this.

Yeah, I'm not worried about the cost on this because it won't cost us $600.

No, it's one.

Yeah, I really don't care.

Definitely.

But again, you see, like, I'm not afraid to spend at all.

Wow.

Yeah, yeah, yeah, yeah, point. You're 100% right.

It's not that I'm stupid, but no, I'm not.

Yeah.

Yes, sir.

Yeah, I'm not cheap. I'm not going to jeopardize our growth, especially if we have it.

Absolutely, 100%.

Yeah, this is going to make us way more efficient.

you I feel this here is, it's lighter in processing than Claude.

Uh... Let me open this here. So,What's going on?

Okay.

Routine, three things to do before tomorrow.

Tomorrow's first one. Start a bot, open a bot, find your bot.

token search with the button send they start Once.

Huh, what was that?

Otherwise, it can't message you. So I should do this.

Start the Telegram bot.

Once, right?

It says here, three things to do before tomorrow's first run.

Open Telegram.

Find your bot. token starts with okay and send it start once otherwise I can't it can't master to you okay go back telegram please Okay.

Right?

And then say start.

This is the one here. Mm-hmm.

Perfect. And then go back to that, the conversation. Go back to the other one. Perfect. What's the next one say? All right.

Okay.

Okay. Let's see. In winter when Chicago switches, okay, this will fire at 7 a.m. I'll flag that after. Remote agent has no access to your local files or settings, so I'll embed all the instructions and credentials directly into the routine prompt, practice the routine. Okay, scroll down. Routine is live. Here's the confirmation. Okay, tenant payment tracker, daily sync.

First run tomorrow at 8 a.m. Okay, scroll down, please.

Okay, so start the bot open telegram. Okay, start. Okay, verify door loop API. The first one will test. Okay.

If it gives a 401, it will try to carry all that time. Run now to test the first thing. Yep, exactly. Run it now.

Running now to test the first sink.

Awesome. Wow, it's even considering the time change, summertime. Oh my God.

Yup.

This is crazy.

SoNo, it's more we can be able to build on it, especially when it comes to notifying you. because I will want it to notify you of What's it called? I would like it to notify you when it's done certain things. Like for instance, like if If it finds, if it had like for a big stuff, like if it sees that someone's late, I would like you to text you that.

you Okay.

Also, I want, I want us to start getting you probably tomorrow, get you switched over to a novate, not novation, notion. So that basically all your tasks could be inside there. And if there's something such as a tenant that's late or something like that, it at least informs you about this.

And I do want it to, and then once we, so we're going to be building everything out in layers. So then I also want to create it where it's actually going to be sending that person a text message.

Thank you.

on like door loop to say like, hey, like you're behind, you're behind on your payments. Yeah.

you Should I click on this link here?

and see what are we doing about catching up.

Okay, let's see here. The test, okay, it typically takes one or three minutes to complete.

The run log will show exactly what is found.

Would it change anything once you see the output let me know what it reports and we can tune anything that needs fixing.

What did the last test run? What did the test run output?

Okay, just. Okay, yeah, go ahead and click on that.

configure trusted domains open yeah go ahead What? Is that what it said? Active.

Yeah, it's on here.

What is this? Oh, it was under routines. Okay, got it.

Sorry.

You're running a daily tenant payment tracker. Ours.

Okay.

Okay, today at 239. Okay, so it's still running. So it shows you at the bottom.

Right there. So it's running right now.

uh Is it here?

Yep, so this one's under routines.

It looks like so we click on routines right on the left hand side.

There we go.

tenant payment tracker. That's where you can actually see it running.

Poor.

Yeah, so it's actually inside. That's how you can keep up with your, 'cause I told it to create as a schedule. The way that creates as a schedule, you gotta go to co-work.

Yeah, Colbert.

Yeah. How about cool?

And then I think that's under scheduled.

Like on schedule? I guess not.

Yeah, go code. See, I think that one has routines.

Yeah, routines. There it is. I guess that would make more sense because we literally built it on cloud code. So one of the things I would like you to actually add to that skill. So remember, it's very simple. You got to-Once you figure out how simple it is, it's really, really simple. you would go into Step seven, is it up?

Is that new? Like missing door loop IDs, guardrails.

Yeah, still running. So, one of the things I would want you to do is that I would like you to add to that skill that Basically, when someone becomes late, Um. for that to be that for that report yeah for you to give you a summary report of of the things that matter such as I would say, so on those dates that you have those tasks, like when you're supposed to check it for it to send you, it's for the email you as well as text you over a report of where everybody's at.

It was.

you Okay.

of a summary report of all the tenants.

Okay, got it. Yeah, yeah, yeah.

Yeah.

Yeah. Does that make sense?

Yeah, so you can be able to see who's late, all that jazz.

Exactly, exactly.

Yeah.

What I want you to do as well is that I want you to create a list of the skills that you're building and cut like so that we could be able to keep track of those.

Similar to what we see on the very first page on the loop, which says overview.

just so that we're not, doing two minutes at the same time. So once we've gotten a skill complete, at least to the completion that we believe, then we can go about building another one. Let's go ahead and not do more than like three skills at a time. And so basically what we'll do is that you complete it out as much as you can. And then you will go ahead and you know, Report it back with me. We'll go over those skills together, see if there's any, you know, refining that we can do together and then you can go ahead and add another three.

But yes, like I said, the best way you could do it is to think back on the things that you do all the time.

you Got it.

Think about what you do all the time. Like, oh my freaking God, what do I got to do again?

Okay.

And then let's go ahead and turn that into a skill. Yep.

Cool deal. I have this bottom here on the right hand side run now.

I think it's already running today at 2:39.

Should I click it?

Okay.

I want to say that it's running. Yes, it runs and it shows today at 2:39 and it's processing.

This one? Oh.

So click on that maybe. Yeah, try to see if we can click on that. Yeah, see?

Click Enable, I guess.

So, Xavier found door loop property IDs but returned empty leases.

Of course I have. Klaus, my friend. Yeah.

Let me try searching my property ID directly. Yeah, so. Right now it's doing its thing.

Okay.

I mean, I don't know what's happening in the background, so. I'm excited.

I can't say I saw any of those that look totally different.

Go ahead and go to the far right and see if you see any IDs.

Nope.

Nope.

Okay. And so, like I said, we can go ahead and while that's running, Go ahead and make a list of all the skills and then we'll go back tomorrow and you know look at this skill particularly but in the meantime we try to add two more but obviously we have to start on our task stuff.

Of course, OK, mainly what you want to answer this one here after finishes running.

Yeah.

Right.

Uh, is do things mainly with a new wall, which is giving me a summary report. And the other one is sending messages. messages through doors Door loop to tenants who are late.

So do this, right, on that list of skills, of the skills that we're adding.

Add. Basically, what you just mentioned, which are the things that you're waiting to see results of. like whatever you're testing out. I'm saying, I'm still testing this out, I'm still testing that out, just so you can take it from your head and you literally put it down so you can kind of know what you were testing the last time you were there.

Okay.

Okay.

Yeah. Okay.

Okay, gotcha. It was different.

All right, brother.

Let me go ahead and make sure. We're all up.

Oh yeah, a little bit different. Yup.

So, but like I said, name the game is trying to keep things as simple as possible, not trying to make things overly complicated.

It was a different meeting, my man. That was different. Thank you. Yes.

Getting to the point, getting to the point. All right. Cool stuff. Well, I had a great meeting today.

Yes.

We were quite quiet a bit. I'll go ahead and Give us our Hope for the day. So it says don't find customers for your products.

Okay.

This is the number one rule of being the best salesman in the world.

Find products for your customers.

Don't sell a product, just know They just know the needs ofYeah. your clients base Yeah. I love you.

100%.

Absolutely. Absolutely. So don't find customers for your products, find products for your customers.

It's basically saying to make sure we find a need and we feel that need. Right now we're finding a need internally, which is that we need something to help us with our daily lives. And then from there, we can be able to expound from that point. So there's different things that we can be able to, you know, Uh... I think what we've done really well is that we have We build processes, a whole lot of processes and structure behind our business.

It's just, there's a lot of structure, a whole lot of processes. But slowly but surely, we can go ahead and automate those structures, automate Those processes and then overall we can then have an AI agent who's who understands each one of those processes and skills and then reports and actually works within them like works within those tasks and might give us back huge summary reports and stuff like that so.

Yes.

Really looking forward to that. Like I said, we're building everything later at a time. Later at a time. So let's do it. All right, brother. Well, I'm going to wrap us up for today. Today is... Wednesday, right? I'm not sure why I didn't update the the one today Yeah, it still has a Tuesday for some reason.

Sure.

Yes, Wednesday.

you Thank you. Well, I mean, it's Wednesday. Wednesday, Wednesday.

That's kind of stupid.

Sir.

Uh, And yeah, so say it's Tuesday, May the 27th. That's kind of stupid.

Okay, but nonetheless, I'll figure out how to automate that task as well. But our goals are still the same for us to have another back-to-back month of $50,000 or more while we generate $10,000 a month in passive, sweet passive income. The cool thing about becoming a millionaire is that they say that it's harder to make our first million, but it's actually easier than to make our first 10. So right now we're trying to get to that first million.

And we're going to work, strive, all that stuff on our way there because there's obviously a lot of skills that take to get to a million. But once we get there to a million dollars, it's going to be way easier to get to 10 million.

Yeah.

As we've been seeing, it's real easy for us to go ahead and understand how skills work too for us to be able to get AI agents. Now for AI agents, we figure out how to automate our whole lives and skills and scale our business up through the wazoo. So, but... Yes, sir.

Let's get up.

So to make $10,000 a month in passive income, while we focus on passive as well as active income streams, as we have U.S. Appointment Center transactions coordinated as well as our IT tech, as we stay focused, diligent, as well as faithful to our goals, bypassing the distractions and staying focused on exactly what's in front of us and feeling excited for what the day has in store because it's going to give us exactly what we want and need, deserve, and that's a successful business as well as life and life as long as we continue to press forward.

these tasks learn AI every single day and just continue to push forward every single day so today is when the day Wednesday we're gonna win day every single day Whole lot of tasks. I don't remember what the last thing that we ended our daily task off with, but make sure we go back to that. And then after such, go ahead and create a list of another two other skills that we need to go ahead and start on.

I'll write the skill down first and then go ahead and also try to what we call it. Go ahead and try to do. Write the name of the skill as well.

Yeah, yeah.

Mm-hmm. Yeah.

Yeah.

Remembering this, you can actually name the skill whatever you want. So the way that you go to it is basically you just click on your name. You make sure you're on that file section, that top left-hand corner. You click that down. You click on what's called Claude. You search for the sub-file called Skills, and they'll drop down all of the skills just like that. Make sure in your studies that you don't get too far ahead of trying to understand every single thing because you're going to easily be overloaded with information.

you only you only learn what's relevant so right now you're under skills so you only want to probably understand skills implementations or whatever so you do not keep in mind do not do not do not download any skills like I did for you from anywhere don't download anything create skills just create them for now Later on, if I find any other skills that's relevant or something that we should be using, then I'll bring it up in the next meeting.

Yep.

Absolutely.

Yes.

But until then, my man, I'll let you go ahead and get to it. It is 2.52. We're at almost an hour past, but I think we did get a lot of progress done, so I don't feel too bad about it. But nonetheless, let's go ahead and have a success for us for our day. Let me know if there's any questions at all.

Let's do it.

And let's go ahead and get it, man.

Let's have the grand running, my man. I'm going to knock off those skills and those quotes.

One day at a time.

Let's go.

Let's do it. I'll talk to you in a little bit, brother. Peace.

Thank you, Josh. Take care, man.
