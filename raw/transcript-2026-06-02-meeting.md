# 2026-06-02T12:46:00.000-05:00

*(Pulled from Notion by the notion-meetings connector on 2026-06-03.)*

---

### Action Items

- [ ] Mustafa to follow up with Veronica about late payment and payment plan  

- [ ] Mustafa to follow up with Ronald about late payment  

- [ ] Mustafa to follow up with Tracy tomorrow regarding bank visit for check cashing  

- [ ] Tracy to contact Wells Fargo to provide trust documents before Friday  

- [ ] Tracy to get check notarized and cashed at bank  

- [ ] Mustafa to post 4513 48th Street property on Facebook Marketplace  

- [ ] Mustafa to investigate if Claude AI can respond to Facebook Marketplace messages  

- [ ] Team to explore Sequence integration using new MCP (Model Context Protocol)  

- [ ] Mustafa to work on automation for utility bill invoice tracking via email  

### CRM Contact Database Migration

- Initiated migration of 16,000 contacts from Go High Level CRM to Supabase  

- Contacts include various categories: sellers, buyers, agents, investors, rent-to-own tenants, title company agents, insurance agents, cash buyers, wholesalers, and private money lenders   

- 89% of contacts have no tags, with inconsistent tagging across the database 

- Only 39 contacts have email addresses despite 16,000 phone numbers 

- Database will serve as a lookup directory for future interactions  

- Planning to create a contacts section in the application with advanced filtering capabilities  

- All contact data will be backed up in Supabase while being accessible through the application interface  

- Successfully connected Railway application to Supabase database 

### Tenant Payment Follow-ups

Tracy:

- Payment of $2,103.83 currently due (without late fees)  

- Has notarized check for escrow shortage ($1,172.98) that needs to be cashed  

- Once check clears, monthly payment will decrease by approximately $20 

- Needs to visit Wells Fargo with trust documents to cash check  

- Planning to handle banking on Friday when off work 

Veronica:

- $600 payment was due June 1st 

- Message sent via DoorLoop asking how payment will be made  

- One day before grace period expires  

- Needs SMS texting enabled in DoorLoop lease settings for automated notifications  

Stephanie:

- Late fee was applied prematurely due to system error  

- Payment actually due June 3rd, not June 2nd  

- Rent due date corrected from 31st to 1st of each month in DoorLoop  

- Messaged to clarify late fee error and remind about June 3rd deadline  

Angel Garcia:

- Initially flagged as late but system confirmed payment was made  

### Tenant Notification System Development

- Built automated skill in Claude to send SMS notifications through DoorLoop when tenants are one day before grace period expires  

- System sends conversational message: "Your payment will be late tomorrow and late payment fee will be applied. When can we expect your payment?"  

- Notification method: DoorLoop mobile app with push notifications  

- System updated for 14 out of 15 leases  

- Skill currently paused pending integration with main application   

- Future plan: integrate into custom application instead of using DoorLoop's notification system  

### System Architecture and Integrations

Current Setup:

- Railway hosting the main application 

- Supabase for data storage and backup  

- DoorLoop for property management 

- Go High Level for some communications 

New Integrations Discovered:

- Sequence (pod) now has MCP integration with Claude  

- Can read bank balances directly through Sequence API  

- Cannot yet create pods or add accounts via API  

Future Consolidation Plans:

- Goal to create single custom application called "Us" that consolidates all business functions   

- Plan to reduce subscription services by building internal tools   

- Everything should integrate with Claude as central AI hub  

### Utility Bill Automation Plan

- Discussed automating monthly utility invoice tracking 

- Plan: Have Claude create dedicated email inbox to receive all utility statements  

- When invoices arrive via email, Claude will automatically update expense tracking  

- Can set up Sequence account to auto-pay utilities, then Claude verifies payments were processed  

- This would eliminate manual data entry for mortgage status and utility expenses 

### Facebook Marketplace Automation

- Priority task: Post property at 4513 48th Street on Facebook Marketplace  

- Investigating whether Claude can automate responses to Facebook Marketplace inquiries  

- Need to train AI on proper response scripts before going live  

- If successful, would automate property listing marketing and initial prospect communications 

### Subscription and Skills Management

- Created skill for subscription tracking that can answer questions about amounts, dates, and frequencies  

- Tenant payment checklist and subscription sheet now running automatically 

- Some subscription data (like seller financing) not yet integrated - needs portal login automation  

- Discussed integrating third-party service company logins for automated data retrieval  

### Meeting Goals and Closing

- Company goal: Back-to-back months of $50,000+ revenue 

- Team roles: Transactions coordinator, appointment setter, and IT tech 

- Focus on building 8-9 figure operation with passive and active income streams 

- Key principle: "The secret of getting ahead is getting started" - focus on taking action rather than over-planning  

- Emphasis on using AI to complete entire tasks, not just assist with them 

- Approach: Build one skill/integration at a time, then mesh everything together  

So, once this loads out what I do is that I'm going to have this saved into what we call super base.

And then I'm going to have it be where all those contacts live instead.

Okay, there we go. That simple? Just straight download it 16,000 files? Okay. Perfect.

That's how many is in there.

Okay, so let me see, I wanna go with...

Thank you. Okay, how about this? I found a better way when it comes to connecting to the people's information. I went ahead and I downloaded a CSV file with all the contacts of everyone inside of my CRM.

even phone numbers that we don't even have defined What I want you to do is that I want you to organize everybodyYeah.

There are possibly a lot of contacts in there in different organizations. Some of them are sellers, some of them are unknown, some of them are agents, some of them are buyers.

investors, some of them are just people that we have. I want them all to be categorized based off of the context of what you're being able to be given. and I want them to be staged inside a super base and so that we can be able to use super base as pretty much our back-end office office for everyone's information in short Go ahead and go through that CSV file.

It wasn't.

internally organize them and then put them everybody into super base most efficient way possible I don't really care so much on the process that you use in order to get organized but whatever you find and beam is the most efficient let's go ahead This will be able to save us from having to go to go high level to it being an internal system.

That's why I thought you were talking to me.

Oh my God.

I hope to God that was the recording.

Okay, so What I want you to do is that I have downloaded a CSV file called Export contact undefined June 20, 26, 12:47 PM. It's a CSV file. Basically what I did was I downloaded everybody inside our CRM And what I want you to do is that I want you to go ahead and extract this and I want you to put it into Supabase. And I want this to be where all of our contacts live from now on.

So, There's a lot of individuals inside here. There's individuals who are buyers. There's people who are sellers. There's people who are rent-to-own tenants. There's people who are...

You know, title company agents, they are insurance agents, they are cash buyers, people inside of our network, private money lenders. There's a lot of individuals inside of it. Wholesalers.

I was like, why is Josh looking to me that way?

But I want you to find a system and a method on and how you are going to you know categorize everybody.

Because I saw it that it wasn't recording.

I mean...

so that everyone is as organized as possible.

Yeah, I mean, guess what?

Find a pattern of systems of some sort, going through all the data, and let's go ahead and upload everybody into Superbase.

Okay, I know that was, thanks.

You thought that I was talking to you like that?

Guess what I replied with? Okay, that's simple.

Because I knew exactly in my mind what I'm going to do.

So I'm just out here telling you to do all that?

That's insane.

Okay, not sure if it's moving or not.

Okay. Why is it not doing anything?

All right, well, So it's gotten everybody you So right now it's looking to add Everybody by tags.

Okay.

It's awesome.

There's about 14,000 people without big reality check before we design anything. 89% of contacts have no tags at all. The tags that exist are inconsistent. Insurance agent versus insurance agent.

Okay. We got the way.

What's this? Yeah, I mean, however everyone wants to organize it.

That's fine with me for now.

I was actually in here at 16,000 at phone, but only 39 have an email. That's a lot. 1.1 have neither the category filled you expect so people How do I connect to SuperBase to load contacts?

One thing I want you to let you know just to get a little more depth of like what's going on. This is just going to be a general idea of people that we're going to interact with. Yes.

So we just want to have it where If there's someone who's already inside of our database, you'll be able to find out based off of their phone number, email, name, whatever.

So, don't have too much pressure on things not being uncategorized. That's totally okay. We can find out a category for them later if we ever get in contact with them again.

So keep in mind, doing all this so that we can be able toAnd And a way for them to remember all these all the gold things that all this actually stacks up on each other so That actually simplifies things.

Yeah.

The point is to look up-it's a lookup directory. Yup. OK. Yup, where it lives, new contacts, cool.

Now, one thing I did want to say is that I don't want the contacts Like, it's okay if we're going to do it like this where the contacts actually are on the application themselves, then that's cool. We just need to have it where... There is a section on the app.

that will be able to keep everyone organized.

because I don't want to be too mixed up with any of our other opportunity pipelines.

That reframes the scope and is a poor distinction that isn't just dump $16,000. You want a distinction You know what? I'm gonna make it I'm going to make this super freaking smart. I'm going to add the same search Let's see if that's filled through.

Oh. We'll be talking for a minute. These approaches, okay.

So, something that I want to be able to do is that Once we create that contact section, I do want it to be able to have an advanced filter section so that basically every field that you have able we're able to search it and filter so that we could be able to identify Certain contacts.

that we want to pre-select.

and there should be a way that we can be able to export them.

You can include any other type of reiterations or things that need to be included as a function. There should be an advanced filter section as well. Go ahead and continue.

So now what it should be doing So. Yes, if we select And if we can do that, We select them to move, they can move, but right now when it comes to The contacts that we are adding right now, there should be a new pipeline or at least is not intended to be a pipeline in a sense. It shouldn't be a pipeline. It's more or less a place where we could be able to view contacts. But we don't want to include any duplicate.

We want to include the contact that has the most information, of course. But That's the thing.

We want to have a section for contacts and we can be able to add contacts, view contacts. We can be able to see if they're involved in any other pipelines or opportunities, but all contacts will live in that one place.

Thanks.

Portal for the payment.

Obviously, all of this will be backed up by Supabase so that the information is stored correctly.

I promise you, like, how much, like...

oh okay so their loop is not just subscription it's per pretend or per lease oh okay so their loop is not just subscription it's per pretend or per lease I can see.

Like this right here, if we can put all this together, it will take a little bit of time, but it will say it was hundreds of dollars per month.

easily $500 a month.

Like creating a scene around.

As well as a, uh,Yes.

hundreds of dollars per month like And the thing is, the way that the other one works, which is Doorloop, it gets more expensive the more people you add.

Hello. Okay. I'll be honest.

I'm not really sure how I can answer this, I want the data to live in super base but also reflect inside of the application as well so that we can be able to view it.

And just so that you're on the same page as well when it comes to what we're talking about. Yes, I know that everything's on railway, but I'm talking about I want there to be a super base integration so that the data could be saved somewhere. So yes, I know what Superbase, I know what Railway is. Unless Railway is like Superbase... which I don't think it is. I think Superbase is more or less for data itself and Railway is more of the hosting platform.

So I do want there to be integration so that the data itself can be saved.

because railway isn't going to be able to save all these people's information But I do want the information to reflect there. Let me know if this all makes sense So right now, it's just trying to understand everything.

No.

your VS Studio.

Which one should help me best with the task, Josh?

I'm so sorry, what was that one more time?

Is it Notion AI or Cloud or VSTudio?

Which one should help me the best with the tasks?

Yes, studio.

notion AI or Claude or the VS Studio, the black one.

Yes.

I'm not sure what VS. Oh, Notion. Notion should help you out with your tasks, but VS Studio can integrate with it. That makes sense.

Okay.

One more panel.

Okay, so right now I'm inside of the Project settings.

And it has general compute and disk infrastructure integration API keys JWT keys login drains add-ons and then it says integrations and then it says data API bolt subscription and usage. Which one of these am I selecting?

None of these actually the connection string isn't buried in the settings list. It's behind the button at the top of the page. Look at the top header bar near the project name. Okay.

I think yes, exactly.

Project means...

For a green Connect button.

Hello.

Click that, a panel opens up with the connection strings. Grab the one that says Session puller or direct connection.

Those.

Oh, what does it say?

connection string It opens up condition.

While you're grabbing things, two more things.

As you've always seen.

I need the real database password to plug it in here. That's the password you set when you create the project. Replace password with it.

If you don't remember it go to settings Oh, okay.

I think so.

So it was like the actual password to log in?

Okay, that was the information I needed.

Okay, so it's connected right now to SuperBase.

Super basic.

That's only if I have it absolutely my free tier.

Yeah.

Monthly fees, is there a subscription? Okay, that's fine.

So whenever we need it, we will do that then.

I just told you.

Cash, buyer, payment, wholesale, entitlement, agent, insurance, agent, contract, a realtor, a team, uncategorized.

Okay, so we're basically starting fresh. There are no pipeline contacts, and I can't go over them.

Give me give the spec a read and let me know if you want any changes once you're good on planning skill.

Man, that's gold. So now it should be.

Evoking the planning skill. This is going to writing plans. So right now it's creating a plan. It's a superpower.

I'm using a writing plan skill to create the implementation plan, treating the proposed category list as an approved and starting SuperBase fresh. No railway data migration since you didn't flag any.

Absolutely.

you I'll note that assumption to write accurate code in the plan.

Let me read the key integration points first.

so what we're doing right now like i said we're just creating somewhat of a A basic framework of everything. Very, very basic. Very, very basic.

Then as time goes on, we actually start utilizing. We're going to see those gaps and we're just going to make tinkers.

Let me improve on the implementation plan. Let me pull the planning skill. Got the patterns I need. Express routers mounted.

Writing the plan now.

Okay. So that's taking a sweet old time in the meantime. What was it that? so I think we already spoke about Veronica.

uh I did.

going ahead and having us speak with her. Could we go ahead and see about creating something like a skill for that.

I did put it in...

College of Fisheries.

in my tasks to create that skill for it.

Let's do this together.

Oh, do the skill now?

Okay.

You guys have time. Go ahead.

Yes.

Alright.

Give me a second, let me look here.

Can you see my screen?

Yes, sir.

Okay.

Okay.

Okay. Okay. So, I don't want to go to a new terminal. I want to pull up the old task that is integrated with door loop.

I think is this one here.

We're OK.

Yes, it's this one.

So I just click here on this one?

So are you talking about opening up a new session?

No, no, no, no, I wanted to...

build up on this old one, this specific one, connect to WP.

Yeah, you can click that plus button.

So weYeah, go ahead.

This one here, right?

Okay. and just build up again from here, build on it, right?

Yeah, go ahead.

This one?

Yeah. You can't be able to reference what that conversation.

Okay, got you.

Okay.

So that's a built skill already.

Um, Thank you. What can I say?

Can I say like I want to add to this skill so that when tenants are.

Late.

or approaching their Due date.

Uh, yeah.

they will be notified and then I set the timings like for example, three or five days ahead before the due date and then on the due date and then when they're late.

Just just just vent to it It's not that deep. Yeah. Whatever you think.

Can you do that?

Okay. Okay, so I want to add. To this skill here.

so that you'll be able to send messages through Duralube.

to notify my tenant.

in three different ways.

so that you will notify them with their upcoming payment That's going to be five days before their due date.

on their loop as well as another Message notification through door loop.

on their exact duty.

And also, Another message Notification to let him know That they have passed.

Go ahead, Claire.

So it says.

No, you just click enter and it expands it.

their due date, by three days.

Oh. You want to expand this thing here?

Let's see if it lets some text.

Okay, that's it. I mean the good thing is it already has the DuraLoop API so Okay.

Okay. Yeah, that's fine.

Does it have an integration with the texting?

I didn't know.

Or is he still finding it out?

I'm not sure, let's see.

How would they do that? I think it does because here...

You're looking good.

This is just click yes, click yes real quick.

Okay.

and then do forward slash BTW.

/btw?

Real fast though, you have to do fast forward slash btw.

What?

Oh, that's a good one.

Oh my God. What should I do now?

Yo, in the space.

Can see it.

Get you space.

Go ahead and click escape.

Please.

What did you want to do?

I just say excuse me, but it's fine.

I'm confused.

Just do-Just do continue Just say continue and ignore BTW.

Forge slash DTW space. You went too fast a little bit. Yeah.

And then I'll tell you.

You can do it right now. For slash btw is not...

There you go, space. There we go. Now just say, Okay, and click yes and say, Have you found the ability to send a Just send the message.

Have you find an ability to send a message through a door loop?

You can use your voice.

Enter.

Yeah.

Okay. Yeah, I know. Okay.

Enter.

There we go, perfect. Now it's answering it without-Ending the session.

It says by the way, it stands for by the way.

I see here.

It does exist except it's blocking one constant type.

Turns message.

Oh, there it is.

Emails, posts, the announcement is the right one.

Okay.

Send emails, text, support a message, select tenants. Okay, good content. Okay, okay, okay, okay.

Cool, the announcement endpoint is the right one.

Okay, that's fine.

Yeah. So just click escape.

One time?

and then do for slash BTW and then ask them whether or not This is whether This will only be sent to one tenant.

I wanted to check with you whether this will be sent only to one tenant or not.

and by SMS So whether or not this will be this message will be sent to one tenant by SMS.

My SMS bye by SMSL is a very specific part.

Okay.

Okay. Here. And then Where is it standing?

It's not whether or not it will be sent to a tenant. It was sent to a tenant by SMS.

Four slides.

I think you can continue the conversation. Just go ahead and continue.

Just. Take a skate.

Just click escape.

Confused.

And then forward slash.

Let's just see.

Actually, it looked like it stopped, so we only have to do forward slash. Just ask it.

When the message sends out, will it...

Cut. Will it send it just to one tenant by SMS?

Okay, that's cool.

Okay, perfect. If I go further, the three notifications you want.

Okay.

SMS only.

So you just went to send them back I was thinking more or less and like I want to have a conversation with them I think, well, I guess, no, it's...

you It's already a conversation.

I think, yeah, I was wanting to see if we can get conversation out of it. But I mean, that's fine. We can start off there. Your run is...

When you text someone through their loop, it acts as if it's a full-thread conversation.

Yeah, because it already tells them.

Just like Go Hai Level.

yeah in a way so five days before it's due no we don't have to worry about the the before it's due only when it's after like so look DoorLoop already sends them messages before their payment is due.

Is it right?

So.

What we need to do is that when they are three days beyond three days actually don't look it's smarter than that right this thing is smarter than that you don't have to tell it when it's due in those when it's due all You don't have to say three.

Oh, I'm sorry, Josh.

I'm not letting them know that they are late. I'm just letting them know the already like the test.

Well, I guess three days after the due date.

Yeah, you don't have to say three days after due date because not everyone's due date is the same.

Okay.

Some people's due date is ten days, some of it's five.

So you could just simply say, for it to reach them.

You're creating a workflow, but you're not creating AI.

You're creating, what I mean is that you're just creating a workflow.

Oh, say this and say that and say this and say that and say this. No, I don't want that. I want it to be where it's a conversation.

I want it to talk to them and ask, why are you late?

This is an incline to ask that right here. So more or less, and plus Doorloop already texts them when they're so many days late. So what is this different?

As the lead like the past The grace for you, do you mean?

The way that we wanted to be different is that we wanted to actually reach out to them to say, hey, we want Let you know that you're passed on your payment When can we expect this?

Okay.

Yeah.

That's a perfect, that's actually exactly what I want you to say.

When can we expect this? So that's one message, as in what he can say.

Let's see, as soon as they're late.

As soon as they're late.

And the whole purpose. Yes. Exactly. So rather than trying to tell it what to say, you want to tell it how to think.

How do you think when you have to talk to somebody? You're pretty straightforward with them.

Do you sometimes have to let them know like, hey, we're about to send you over a notice to quit?

You should. Here a little bit Right. So, um, so you want this to be your assistant. So should it know that you usually send people notes to quits? Yeah.

I should know that, hey, Weeson, Hey, we still haven't been able to contact you.

Now, should it know What's it called?

Okay.

checking with you before it sends these messages it should probably do so Like you should probably go ahead and check to see whether or not the status has changed or anything like that.

But when it comes to any type of updates and such, It should have a skill where it should try to go ahead and updates you with that information.

Okay.

So just to keep it simple, right? Just to keep it simple.

Right, we want to have it where there's a conversation being the whole intention is to see how, when are they going to pay us?

But in this case, I need to teach it. the process and the steps of escalation.

Right, what route, what specifically?

Which one?

are they going, when they're going to actually pay us, So that... they can stop further acceleration. at this point. And acceleration is them being pretty much evicted.

Oh, yeah, yeah, I see that.

essentially.

See what I'm saying? Yeah.

I know there's a lot.

I mean, you can just simply, if like, What you could do is that you could just give them that... You remember that time we sent that thing to Veronica?

We sent Veronica over a screenshot showing her what was coming up next.

So look, So this could be a lot simpler, right?

Okay.

Okay.

uh, So thanks them only when the past the Greece period, right?

You could just go ahead and download that file, right?

And then you can go ahead and say, hey, check out this one file. This is the escalation. This is how we escalate everything.

everything and we want you to stay on top of them. We want you to text them.

Okay.

letting them know that, hey, they have this coming up.

How soon can we be able to hear back from you? Just keeping their words pretty short and brief.

Absolutely.

Okay, so we need to do some modifications to our I'm sorry, Josh, go ahead.

Start when they're halfway through their grace period.

Okay.

Process so that you would Send them an SMS message through door loop.

actually no they have one day left of their grace period when they left the grace period actually no they have one day left of their grace period when they left every spirit Thank you.

In a conversational so that when they respond, you would respond back and so on.

And that would be only when...

They have one day left on their grace period.

I think I'm gonna leave that on there. Great, spread.

And the SMS message would be. in lines of Your payment will be late tomorrow and late payment fee will be applied When can we expect it?

It's going to late payment.

Fee will be applied.

When can we.

You said, what was that?

When can we expect your payment? Uh, One day to the grace period to be over. And then it's going to say exactly your payment will be late tomorrow and the late payment fee will be applied.

That's true.

Yeah, you can do that.

When can we expect your payment?

Okay, when can we expect your You have my number inside the door loop. I want you to Tell me the best way you will get me notified when they reply back every time.

Should these go SMS only or do you want? Okay. Wow. This is going to be awesome.

Whoa.

Is it important to leave now? When can we expect your payment? Finance, Conversation and Tiers. Okay. Every time they're fine.

respond to one of these, you apply, immediately advise you by SMS, email with a message and respond No.

AR response first, then I advise you.

by generates response on your behalf sends it to the tenant and then it gives you the full exchange. So it's there.

Forget an NFI. Here are your options.

your loop mobile app,And And yes, I will download The door loop mobile app. Josh, are you following? Are you following? Okay, so It will let me know before it replies back.

and it requires me to download the Duraloop mobile app.

So that's not a big deal. I'm going to do that.

I feel like it's going to be useful.

Okay.

And it's going to reply. I'm sorry, it will initiate the very first message within this conversational thread, Only when they are one day before their grace period.

That's fine. Just make sure that the emails are What's with the devices?

Oh, it's on my TV. Oh, okay.

How do you feel about that?

Are these messages-Okay, cool.

Oh, actually, it gave me a few options, but it's recommended the best way, which is I feel like it is the best way, which is me having the Duraloop mobile app.

That's fine. We can do that for now because eventually we just need to all go through our system.

Yes, but I'm saying that this right, like it going through door loop is something that we're going to try to change so that it's all done internally.

It's innocent modification.

What do you mean?

No, it takes a while.

It's only the notification.

And then I have to explain it to you as well.

Okay.

Can't we just do it now?

Okay, got it.

This is something I'm glad you're having this like this is a nice beginner. Let's just get it started.

It's like a good warm-up. Got you. Okay.

Okay. Okay, here's all.

I think there's the API key. We have the permission on WA. Okay.

Oh, yeah, sure.

Okay.

Okay.

I just downloaded the Duraloop app.

You just said, okay, so you said that right now it is...

Yes.

So is it going to have more of a conversation with them?

It will tell me first.

So what would it do with the responses?

It will show me that before it responds.

Just in case if That's another option was there already.

It should respond back like on its own.

And then it should just tell you about the results of the response.

I can choose it, but I'm afraid it will mess up. I mean, I don't know what they're going to respond with.

I want to test it first.

We can try to.

What do you think?

Her payment is late. So her payment is late tomorrow, so that's the biggest thing.

Okay.

Yeah. That's Veronica, right?

OK.

Okay, let's see. Create a success video. Did you receive an SMS on your phone just now?

I didn't know, whatever.

Was that on through door that it said that message? That's the question.

I didn't get it at all. Neither on the phone or their loop.

Or Go high level number. I mean, I didn't get anything.

I mean, maybe it's on the number. Let me check.

I will go with option A.

Thank you. The messaging through door loop option B was, uh, through its value, You don't want that.

Okay, so Still having issues with it sending a message to Veronica Oh, God.

It's not Veronica only, it's a skill.

Got you.

You said to build a field, right?

Got you. Got you. Got it.

Yeah, for everyone actually who has one day only for the grace period to be over.

I feel like it's almost done.

You can send the BTW, but that's just as a heads up that that's possible.

I mean,Let's give it a bit.

I mean, what does that mean?

Like, uh, technical wise. I mean, what was the purpose of interrupting it?

It's just as a question without interrupting it.

You will never believe it.

And you were happy about it.

Oh, goodness.

Five days before due, but That's already, I don't understand why that, Why do we Okay.

Okay. It's all done for 14 leases out of 15.

No, no, no. So five days before due needs your setup because I told it precisely to ignore it for now or don't do it. So what's done is just one day before grace expires? And it says here after grace expires, I don't know why. Which is fine, I'll be honest with you. But the thing is, it's updated for 14 leases out of 15. There's an issue with one lease. Guess who's that? It's Veronica.

Okay.

laughter it says here it needs a manual interference I need to go to the lease in It's active now.

you OK, let's do this. Let's do this then. Because I think this is way more efficient. Is this active right now?

So Okay, got it.

We just need to enable texting under Veronica's profile and then That's it. It's good.

All right, let's do this instead because I think this is probably, okay, you know what? No, I'm gonna let you do your thing. I'm gonna let you make it work. Make it work. Figure out how it works and we'll figure out a more efficient way to do it later. That's fine. That's fine.

Okay.

I mean, it's done. It's live. I just need to enable texting under Veronica and we're good. That's it. Okay.

Go to lease door loop settings, late fees, enable text. under remind tenant before late fee and after late fee and that's it.

settings please Okay, so I fixed the issue only for number one, for Veronica. Because they really don't want the five days before due or on due date.

Okay.

at all. Okay. All good. Up and running.

Let's go, let's go, let's go.

Okay.

Skill updated.

Here's the complete final state of everything, blah, blah, blah. One thing to keep in mind, any new tenant you add to DuraLoop in the future, just make sure their lease has... text checked under late phase reminders in their loop since we can't set that automatically via the API key. We just need to tag the two checkboxes for the SMS notifications.

So this means that any Lieutenant, the system will apply or this skill will be applied to it automatically, which is awesome.

Yes, sir.

Okay, perfect.

Okay, so One day before grace period, not just a notification, that's a whole conversation. And we will be notified.

Okay, give me one second, Josh, I'm sorry.

I want you to do a live Test run now for anyone, any tenant who's late and he has only one day on their grace period.

Okay, I want to see a push a conversation over to Veronica.

Let's see if it works.

Gary.

Wow.

We're going to be building a lot.

I mean, I could do it, right? But the time I consume now building this, I consumed it once. You know what I mean? And then it's going to be running.

Actually, make the same.

And then build something else and so on.

Yeah.

Oh, so for some reason, Josh, it says here.

Is Angel Garcia?

Can you see this table? Still checking.

But that's impossible because he paid.

Okay, you know what?

Okay.

This is probably back to my point. Let's just go ahead and make this... Just because of how long I'm seeing this one is taking specifically. Let's go ahead and...

We're just gonna make this we're gonna do this I know exactly how we're gonna do this as soon as I get this all these information connected to the app that we currently have in place.

Gotcha.

Okay.

So we wouldn't need this here?

then what I can do is that I can say it already has the ability to text message.

on there.

And so I can have it where We could just have where we can see the status from door loop.

Is that what you're saying? You're saying that we wouldn't need this here, this skill?

Talks to the application and then it texts them through there and then we can be able to actually visualize everything the way we need to.

Yes.

What was that one? Yeah, we wouldn't need that skill, right? Not right this second, not right this second.

Okay, I mean, it's already in place and running.

Told you.

Um, If you won't need it, so we might need to like delete it or switch it off.

Just have it. You can tell it to do that right now.

We're going to utilize something very similar to this as soon as I get this done.

Okay, gotcha. Okay.

I'm happy it was evil.

We are. We are. Yep.

Got it.

Okay, I just want to say heads up. I'm happy it was able to see that Angel has made the payment.

So that's cool. Yeah, I love it.

All right, I'm going to tell it to...

Stop.

uh, Until further notice.

Okay, cool.

Thank you.

I just stopped it.

Perfect.

That's a really good question.

So For the payments, I needed to speak with McKinsey really about Veronica and Ronald.

What task from yesterday, while that's doing its thing, what task from yesterday do you have any questions on?

And Go ahead.

I couldn't speak with her.

Go ahead and Go ahead and reach out toWhat I call it, Go ahead and reach out to What's it called?

So I'm trying her today again. And I'm actually speaking to the tenants themselves.

Go ahead and reach out to I'm trying to remember.

Oh, yeah.

I mean, I'm reaching out to his talents anyway, so...

No, yeah, just reach out to tenants personally. Yeah, that's exactly it.

Yeah, yeah, that's what I'm saying.

I mean, I'm going to try her as well, but even though if I spoke her or even not, I'm going to still speak with Veronica.

on her own as well as Ronald and Samantha.

I have a task for that. So are we good?

Uh... Tracy actually is due yesterday.

I did speak with her.

Josh, do I need to speak with those who were Jew on the first?

Yes.

Okay, so I have few actually.

Hold on, hold on, hold on, hold on.

Why is...

So we have, Who's late?

Who's the lady right now?

Tracy Ronald Davis.

Yeah.

Ronald?

Late as late, Ronald and Veronica only.

What's going on with Stephanie?

What? Hers is late too.

Hold up, her amount looks different right now. Why is it $9.52?

Oh. That's not right. Why is her stuff showing on the... That's not right.

That's not right.

Thank you.

No, go ahead and you, I'm not sure what happened.

I'm not sure what happened. Yeah, let's go ahead and make sure that's going correctly. Take that lady off the stage.

Go ahead, Luke. to make that paint.

Delete that. Yeah, I'm out.

Let's also make sure that her rent is due on the first of every month because not 30thThe shot right now that is on the 31st, that's not true.

Okay.

you It's showing it. It's yes, sir. Okay. So this should be I got you.

I'll be on the first.

So change that right there from, yeah, let's do it. Yeah, perfect. Okay. But the only issue is, is that But the starting is February 1st.

Not to mess with the...

Contrast 30.

That's what's going to change, I believe. There you go.

There you go. Okay. I'll save that one.

Yeah, go ahead and send her a text message to let her know that we saw that there was a, that there was a small error.

okay uh create new Okay.

Because it was Yeah, so just go ahead and send that over to her communications, please.

Yes, please.

Just say, hey, this is-Yeah, I'm noticing that your payment is going to be late till tomorrow.

Oh.

Will they be able to make this?

Yeah, just go ahead and answer that. Tell them that, That late feed.

No, it is.

was premature because that's actually tomorrow but Yep.

Okay.

that We noticed that late fees got applied to your profile.

Good night.

Okay.

See you in the ride.

Bye.

Okay.

Let's see.

Pay to your payment. Then, fixed.

However, this is Heads up.

Hey, Stephanie, we noticed that a late fee got applied.

prematurely to your payment.

How long?

What you guys have the payment for today will you guys be able to make this payment today?

We got that fixed. However, this is a heads up that your payment will be late as of tomorrow, June 3rd.

Uh, I can say, like, make sure to make your payment today.

Yep, please make sure to please make sure.

Just say please make sure to make your payment today.

Please make sure to make You are.

today.

Okay. Gotcha. Boom.

Oh, wow.

Failed to send message. That's nice. I mean the previous one.

The previous message by the system that said you have late fees applied wasn't sent.

Go ahead and send this, go ahead and send a message over to Veronica, please, as well.

So that's...

Oh, okay.

Create new.

Okay. Hey. Veronica? This is A reminder about your Amen.

Take off the hat.

Um, 600That was due.

Do you know what that is? Take the hay off. Veronica, this is Ramon.

on June first Everything is up.

Your famous. Peace. as of tomorrow Make sure to...

Nice.

Make your Amen. Today. to avoid May it feast. to the world.

JuneThird.

This is a reminder about your payment of $600 that was due on June 1st. Your payment is late as of tomorrow, June 3rd. Make sure to make your payment today to avoid late fees. I mean, it's...

No, no, no.

Check out that part right there about making your... Will you be making your payment? how will you be making your payment? So how will you be? just say how will you be making your yes to just say that your payment will be late as tomorrow how will you be making your payment Your rent will be Like as of tomorrow.

Okay.

Don't mention life ease?

Okay, how will you be making Your payment.

Okay. That's it.

Yep.

Okay. It's cool.

Do you prefer me communicating with those guys here? through the loop instead of go ahead level? I mean specifically if it's a follow-up question.

I was.

I would say yes. Yeah?

Especially if it's a follow-up on a payment, not anything else.

Yeah. When was the last time you spoke to Veronica? Have you been giving her a call or you only been speaking with Mackenzie?

I've been speaking with Veronica a lot, actually, but up till...

I need us to go ahead and speak with her today.

Yogi.

The last time she made a partial payment to McKinsey.

Not after that.

Yep. As well as the other girl as well.

Okay, that's fine.

I have it on my task already.

She had a task separate from Ronald.

Huh? Yep, Ronald as well as, what's the other one?

Vino?

No.

Ronald, right?

She's in Amarillo's.

for 2802 Yes.

Samantha?

Oh, Tracy.

Yes, I have a task for you as well.

No, actually, I'm on very good terms with Tracy.

So Yep.

Okay, well, uh, As long as we have this Oh.

We're good. Okay. I'm calling Tracy, I'm calling Tracy.

Hey, Tracy, how are you?

How are you? Doing well, doing well. What was that?

I need to send you guys that notary thing. I got it notarized. I've been really busy and I'll take it out. My dad cleaned my car, so it's like somewhere in my car.

Well, that's more or less so you can be able to cash that check. You don't have to give us the notarized document.

Well, stop committing it like you guys needed it.

No, no, I mean, well, we just need to... Well, if you were wanting to catch up on that, uh...

On the pad wall, I guess on the shortage, that's more or less what the the notary was the notary was regarding you cashing the check so that you can be able to catch that up but as of today um there is an amount that's old and so I just want to see how everything was coming along with that Yeah, I've seen that.

Is it still the same? Because remember we made that invoice in May that it's supposed to be for June?

We made the invoice in May that it's supposed to be in June.

What was that?

'Cause it's showing that I'm gonna have late, that it's already late, like past 10:00.

to these leads.

Basically.

No, I'm looking at it right now. Mustafa, go ahead and pull up her account real fast.

Mustafa, you can take yourself on mute.

Yeah, he's pulling it. He's pulling the statement right now. We're just going through this.

Yeah, so as of today, it's showing $2,103.83 as of today, which is the correct amount as far as what the balances are. Now with You signed a...

That is correct.

That is still correct. Yes, sir.

So with the--How's it $100 late if it's barely June 2nd?

It's not $100 late. This is without late fees.

Oh, okay, how much again?

so two thousand one hundred three dollars and eighty cents yeah yeah but I was getting messages or a notification where it was saying that it was I was already like 10 days late.

Go ahead and bring up, communicationWhat's that for?

So you were getting text messages?

I got a message in like an email Let me see if I can find it. Hold on, because I've been having so much shit come through.

I remember I seen it.

Thoroughly, okay.

May 31st.

Urgent link.

Urgent link. Settle your rent balance now. $2,314.21 due on May 21st.

Go to, um, Mustafa, where you on goal? High level for, go back to door look, please.

Go ahead and click on where it says transactions.

And then I know we were just setting up your account.

Mm.

yeah i'm not seeing anything on i'm not saying that you're obviously obviously reading something off um but i know that we had just set up your account on door loop so but there's no there's no late fees of as of right now there's there's nothing let me go to the actual app because that's That was something I was going to say to you.

Okay.

And if that continues, let me know. But I'm not seeing anything that's being sent. I'm looking right here in the communication where it's supposed to-Show all the transaction.

Yeah, I see it.

Okay, yeahI see it now.

The only thing I can consider or think is that because we just got you set up, I know sometimes we're doing some manual adjustments because it'll especially when we have a leap year where February just comes around the corner and kind of messes people's dates up.

But no, as of right now, everything is pretty much straightforward. Now, as of today, the amount that's owed is $2,103.83. That's just pretty much what everything is. But with the shortage...

Take it off.

No, this is, well it's nothing, the shortage isn't taken off because nothing's been paid towards it.

Yeah. Nothing additional.

So with you...

About that check being cash, I'm I'm supposed to be going out of town on Friday, so I just went ahead and requested for me to have the date off.

I can go take care of that on Friday for sure because I won't have to worry about it.

Okay, okay.

All that other.

I would, let's see here.

So you're getting the document notarized. Now you also need to-I got that notarized.

okay so you also need to bring your your trust document as well.

And then What I would recommend is for you to go ahead and take it to your local bank. Now, I know you're saying that you're leaving on Friday. I would, I mean, this is just up to you. I would recommend you to, if you're trying to get this done sooner than later, it just depends on your availability and I know you're a working person.

Um, probably to go there to your bank to let them know about the situation I would say that before I would do that maybe a day or two beforehand. So today is Tuesday. I would try to, if you can, to swing by your bank tomorrow to give them your...

Yeah, because the more you can be able to do this beforehand...

And you could be able to speak to that banker or at least you could be able to say that, oh, I've sent them this these trust documents ahead of time. I'm just letting you know, because those front desk receptions, they're they're they're taught to be when things look out of the ordinary, be extremely cautious, be, you know, you know, they're just going to make it more difficult. But if you're saying, hey, no, I was proactive.

I already sent you guys over this. You guys already have this on my file. Go ahead and pull it up on your end.

Okay, this is a little weird, but you already have it on file. I do see your name. Can I get a picture of your ID? This looks good. But I'm just saying, if you try to do all that in one fell swoop, I can foresee...

just some pushback from the bankers a little bit.

Yeah, no, I'll do that. I'll call him. I'll let him know.

Cool, cool, cool, cool. All right. Let's see. I think the only other thing besides that, I'll have Masafa follow up with you on this tomorrow. You and your mother, are you guys both, I mean, obviously I know that it's kind of weird a little bit. Just so I can get a context of what's going on.

Has she tried to reach out to you?

She spoke to me about Last week, the Thursday.

understand last week.

'Cause I know she started I know she started her, her couple of music band where she was sitting there crying to my brother and he said,I like that.

If I told them I said bro, she'd-Break this down. Like, I have messages from Josh where he's telling her she's...

Oh, yeah, you closed it 30-something days late.

And she's like, I've never been late. So I'm just like, it's a mess.

Okay, I understand. Well, I just wanted to, well, if it's pretty much just saying that, you know, hey, we have a disgruntled mother, you know, and, you know, she's just, she has your contacts, she's reaching out. So I just, I just wanted to, only thing I wanted to know, basically my conversation with her was that, you know, well, at first it was geared towards me saying that I had, I was trying to force you out the house or something like that.

You know, I just basically, and she was wondering why I was communicating with you, and I just told her, well, she's the only one who is taking accountability for the house and the payments on it. So you're the one I've been speaking with. So, but nonetheless, I just wanted to see if you guys were or were not working together so that I know kind of how to, again, I'm going to play the dumb role either way, but...

just so I can understand what's going on in big picture so big picture She's sitting here.

I'm telling you, she wants to make a payment. I mean, that's fine, 'cause that's the last money I got to work out. But as for anything else, I know she did give my brother...

$1,000.

Okay.

She's like three months behind.

And we're taking care of most of the shit. Right.

yeah soOkay, yeah, no, I just wanted to make sure we were all on the same page.

And that's pretty much it. If that's the way that she works it out, that's great. I'm just going to send her to you just as a heads up.

Just tell her, well, I have her blocked. If she tells you anything, you know what, contact your son.

You said you know how to get a hold of your daughter.

It's not my problem. I just know you guys pay me that day.

Okay.

Got it, got it, got it. All right.

I know her very well. She's gonna, whatever person she can bully into giving her information she will do it Understood.

Understood.

All right. Well, let's see here. I guess tomorrow we can just follow up with you on.

you getting in contact with The bank, you said it was Wells Fargo, I believe.

Yes, and I'll try to contact Ben here in a little bit.

First thing in the morning, Uh,For sure.

Okay.

Well, if we can get on that sooner than later, As soon as we make that additional payment towards the escrow shortage, we can reflect that like same time yeah so that that's that's almost I want to say 20 bucks or something like that off of what's showing right now Okay, that'll work. Excellent. All right, I'll let you do your thing. Thanks so much. Okay, thank you. Bye-bye.

Cool. Let's follow up with her tomorrow, please.

Yes.

Veronica, you haven't spoken with.

Okay.

So I have three. three, separate tasks for Veronica, Ronald, and McKenzie.

You said he's been a mess. Let's hound Veronica. I need to figure out whether or not she's planning on making that payment because.

We worked with her at this point.

So even if McKinsey picked or did not pick anyway, I'm going to speak with Veronica as well as Ronald.

I just want to see you, babe.

Are you paying? Are you not paying? What's going on?

Okay, perfect.

Yes, sir. I'm going to head ahead for today, so I'm just going to...

Let's do that. Besides that, what other tasks do you have? So did you write down that? Okay, let's make sure we... Did you write down the one with Tracy for tomorrow?

No.

Uh,There is it, so tomorrow?

Yeah.

Okay.

Thank you.

Tracy, there she is.

Oh.

Why is it showing June 10th?

Oh, it should be June 3rd, okay.

Okay, that one is good, as well as for Veronica and Ronald.

Okay.

But only Tracy is pushed to tomorrow. Veronica and Ronald are today.

And yesterday when I spoke with Tracy, she was asking if the 210383 will go down because of that check.

I told her no, not this time, because technically speaking, it's not cashed yet. So you will need to cash it first.

so that we can know how much your monthly payment will go down by.

Yeah, I gave her the amount, which is $11.72.98 for the escrow shortage. She said the check is $12.

OK, got you.

hundred something I think 1209 or something And then I told her about GenieScan so that she can send us a scan copy.

Got you, got you, got you. Okay, perfect.

Any other questions?

As she said, she already signed it and got it notarized. So we're good.

Nope, I was able to build the skill for the subscriptions Any kind of question you have in mind?

Okay, got you.

for subscriptions, amounts, dates, frequency, AI related or not, anything crosses your mind, you can just ask it and to respond right away.

The only, but besides what though? What other things are not being included?

And now, tenant payment checklist as well as the subscription sheet are running automatically I mean, nothing that I can think of.

What do you mean?

So for subscriptions, there are a few fields on the sheet that are blank. For example, I need the credentials for a few of those subscriptions from you so that I can jump into it on the websites and get the amount because There's some subscriptions.

Subscription sheet.

I'm not sure that's what I'm I'm talking about more or less The seller financing, the seller finances as an example.

Uh, Amounts on the sheet are blank.

Just do those reflect or not?

So, I wouldn't know it unless I logged into that subscription's website, you know?

So the door loop is reflected automatically to the sheet, correct?

But the dates that Seller financing reflect on what?

Door loop. Sean Okay, but solid finances are not.

I'm confused.

Yeah.

Okay.

Oh, I'm sorry.

I got your question. Okay. I was, I was thinking about something else. No, sir, not yet. I will need to still...

And so you read that.

So the skill will need to log into the portal, which is I think very simple.

Okay, cool.

It just didn't embed it that yet, didn't integrate it yet.

We can do that, we can do that.

But it's very, very simple.

I know how to do it.

Yes, exactly, exactly. For it to basically be like that, yeah.

Don't worry about it.

Yeah.

You're talking about the third-party service companies, right?

I mean, I had to do it on my end.

Okay.

Yeah, yeah, for sure.

There's like some innate in things and stuff like that. Like there's a little bit of a process, but it can be built.

Okay.

Excellent, excellent.

I can work on that.

All right.

What else in terms of automation or or skills that you see is going to be a priority for me today?

Oh, you know what? You said something about the pod for sequence.

If they can be able to, But if there is a way for us to be able to create, and when I say, is there a way that means to build it with AI, right?

So.

N-A-N. Well, I know N-A-N is one. Let me go ahead and share my screen real fast.

I downloaded it by the way.

Just to see if there's any deliberate Integrations.

But I'd never used it before. N-A-N.

Don't know what.

What's that called?

Oh my god.

Oh my god.

That's why.

It has it. They just built it.

Hey, just built it. Thank you. MCP is Oh my god, they got it.

It wasn't there?

This is brand new. It's what everybody's been yelling at them for.

Okay.

They got it. So this is the integration.

What can this key do? Everything. Wow.

Oh, my God. Now I'm thinking what I can use it for.

Oh, okay.

I can see the whole sheet is lighting up Let's do it. And we both can use that key, right?

Yeah, yeah, we can.

So I'm gonna put this in the chat real fast.

Don't worry about that one yet. This is how it works right here.

Awesome. Okay.

Mm-hmm.

So that second one I sent you, that's the NCP.

Okay.

That's literally for cloud code.

Like what do you get? All of this? All what you sent me?

Did you get the clock?

Yeah.

Okay.

Now, here's the thing it has to be, you have to be careful with is like it.

I don't think it has the ability to create though. Yeah, let me see.

A pod you mean?

Which is awesome.

I mean, that would be silly. It has the ability to just transfer. Yes.

That's really good.

And then it has the ability to... to read as well.

Yeah, that's just go ahead and give that to it and then figure out how we can make it useful. Jesus. Yeah, go ahead.

Just do it.

I would like to see you can create a pod, but I'm not sure if we can add an account. I'm not sure if we can add an account.

Okay.

I mean, just ask it. Down there on the right-hand side. you you Yeah, yes.

So API Trigger rules, one time, yeah, I don't think it can.

It can't create, it can't create, Sugar rules.

Just came out. What does that mean? Yeah, they should have...

So it can actually retrieve... Oh shit!

Bro.

With this we don't need to have, oh my God.

Well, you don't need... You can read the bank balances off of this.

You can read the bank balances.

But it won't be able to see the destination, right?

You can read the bank balances off of this.

You don't need, you don't, now when it comes to transaction history, You won't be able to get that, but you can get the bank balances, which is...

Still very helpful information.

Okay.

That's really cool.

You're welcome.

Oh, you said what? Oh yeah, no.

Okay, let's go ahead and just use it, see what it does.

Wow.

I love that. Okay. Like just give it to Claude and see what happens.

Yep.

No, no, no, no, no.

Yeah.

Oh, okay, got you. But that's what That's with flawed code through VS, right?

Just give it the integration and then ask it, you know, what can you, this is with sequence, what can you read and what can you, like, what is it allowing you to do? So we can see what Yeah.

Not the basic code. Okay, got you. Okay. Got it, got it.

Yes.

Okay, there's a big thing here.

Absolutely.

okay cool deal well I say for now let's go ahead and wrap this thing up Right now, I am...

Mm-hmm.

Still letting this thing-it's actually-Like I said, it's adding everyone inside of the application. It's using a shit ton of points.

What's important about it is that we can be able to use it with other applications as well. So like for instance, notifying individuals. That's why I said Let's put on pause.

because it has everybody's information on here. So that's one. Think about everything can speak to everything else. So it's just like, okay, well we want new applicants inside Doorloop.

Yeah.

to be at least to make sure to verify, we can verify that their information is in there, boom.

It's just me asking you, I was telling you, I'm going to add those context one by one into Notion.

Like so.

Until we create our own door loop, we can make sure that their information is shared.

Because they can't do that.

So Yeah.

And you told me like, hey, stuff here is so stupid. Just ask AI to bring it over from GoHideLevel.

Okay.

So that's, that's the, that's the whole intention is to see how many tasks you can be able to, to acquire or do through AI, everything, every single thing you're right. If you're thinking about it from that perspective, you will become a lot more creative. You're going to think out outside the box when it comes to Your questions and your statements and things such as that.

Got it.

So that is not what you can do. What can AI do for me? That's the biggest thing. What can it do for me?

So yeah, so as much as possible, you should be like, Like, okay, well, I have that task. Okay, let me create a skill. Now, once we get to the point where we went through a tremendous amount of skills, tremendous amount of applications, things such that, then we can start trying to mesh everything together even more.

And then once we have all that together, where we're, we're, we're, we can pretty much function within cloud for the entire business. We can function within cloud.

Thank you.

Then that's when we can go ahead and hand it over to an AI bot.

Yes. I feel like it's exactly the same as you telling me, just speak.

But the craziest thing is that once we don't have to be that organized. That's the whole point. We don't have to be that organized. We just need to. The skills is the most important thing in the connections. We can make sure the connectors are there and the skills are there.

then we don't have to be that organized.

Just talk and don't worry about typo or anything not in order. It will organize and build whatever you tell it to do. Yes.

Get it.

We can just we can brainstorm everything with AI. And then because it has connections to everything, it will be it will find the most efficient way to be able to connect to everything. We just got to give it a big period at this point.

And that's it.

Exactly, exactly.

Yeah.

So, like I said, my goal, my ultimate goal when it comes to everything.

Everything's in the house.

Everything but Claude It's us.

Got you.

Okay. Wow. We're going to name that application us.

Yeah. I'm sorry, quick idea. I'm sorry. I know you're in a rush. Usually what I do on a monthly basis, I fill in the sheets for mortgage status and the utilities on the sheet. And then I pour it into the expenses and door loop.

I'm gonna try to work on something so that it would be done Good morning.

There's no subscriptions anymore. I'm talking about like literally from what I've seen, we probably need to go through all of our subscriptions and every other like there's only a few other things besides like hosting platforms. Yes, there's a like like railway. That is something I probably do need. Super Vegas is probably it's like more of a data place where it has a data. But, you know, there's some other subscriptions I probably have that we don't need anymore.

Please do.

create an application for I want us to create an application for And really my main goal is Everything to be inside of as much can be condensed into one application where it's just us.

Okay.

It's literally, it's completely custom to what we do.

Yeah.

Connect what?

For real, yeah. So, I know exactly how you could do that.

I can tell you exactly how you can do that actually.

So the way, the way, the way, the simplest way that you can probably be able to do that is connecting to, to docs at Weber investment homes.com. That's one, right? So connecting to docs at Weber investment homes.

And then, So the statements, or you know what?

genius idea way easier and actually a lot more integratable have the statements go directly into Clog.

Let's watch the dogs.

ask Claude to create an email Inbox it can receive all the statements.

directly Oh.

No.

Okay, but it will need to look over Docs mailbox using zip here. Most in place.

No, no, no, I don't think you'll have to. No, no, no, I mean, like...

Oh.

So this is what I'm saying.

They send out an email every single month of what's old, right?

Yeah. Okay.

I'm saying that the same way, think about it.

Claude just emailed you.

Yes.

You can reply back to that and clock read it.

As Clouds create an email You can have the inbox that the all the so basically you just need it you need to figure out how to redirect the emails they're being sent out not the username just the emails so the emails gets into a certain thing for all the utilities so all the utility go to a specific account.

Okay.

Okay. Okay, good. Get it. Coming.

So now, The cloud is receiving the invoices as they're coming out. So as soon as it receives it, it knows what is this? Oh, I know what this is. Let me update this. And that's the cost.

Yes, so as soon as the invoices are are due.

I mean, I created it will at least know that part.

Yes.

Do I have a specific card?

Now, how will it know that the invoices have been paid? We can probably create literally, we can probably even go as granular later as creating a sequence so that all like the like... All the properties that have let's just say utilities, right?

Got it. Exactly.

We can. Yes, it can have it where the money just goes into that account.

Yes. See you then.

How does it know we're cleared? Because it knows that zero.

It knows when it's supposed to be pulling out.

And so, I know I'm going to check to see if it's been pulled out and it will check, boom, it's been paid.

Okay.

Yeah.

Yeah.

That's how we do it.

Exactly. Yep. So,Let's go ahead and do it.

Yeah, we can make use of this new update on Sequence. Yeah. I have a lot in my mind.

Okay brother, we got to jump off.

I want to put it Here, I know.

Yes.

Yes, sir. All right, man.

Tremendous, Susanne.

Yeah, it's the tactical Tuesday. Yeah.

I'll go ahead and wrap this up. Mr. Mustafa, our goals are still the same for us to have another back-to-back month of $50,000 or more. We're having the transactions coordinator, appointment setter, and thank God, finally, our IT tech. As we continue to grow this into an eight, nine, and eventually 10-figure operation that's focused on passive as well as active income streams while we stay focused, diligent, as well as faithful to our goals, bypassing the distractions and staying focused on exactly what is in front of us and feeling excited for what the day has in store for us.

because it's going to see our effort, our energy, and our consistency, and give us exactly what we want in return. And that's a successful business as well as life alike. All right, today is Wednesday or Tuesday?

Tuesday.

Three is Tremendous Tuesday. And for some reason, my dad here hasn't been...

I like that. I like that. Okay, let me see here. I'm going to ask you for a quote.

Okay.

So I checked my task and it seems like you have not Updated my task to reflect today's date.

or my the other things but before you update anything give me the quote of the day so I can wrap up my meeting Hmm.

Okay, never delay.

Yeah, that's real. So the secret of getting ahead is is getting started.

Never delay today's work till tomorrow.

Ha ha ha ha ha! That's real. Yeah, so the secret of getting ahead is getting started.

Sir.

Absolutely. Yeah. Yep. Sorry. It's to continue to do it productively and efficiently.

Yup, it's just getting started. That's what we're doing right now. We're trying to get ahead of a lot of stuff right now and ultimately we need to go ahead and just get started. That's what we're doing. So, cool deal, man. I'll go ahead, I'll let you do your thing. I'm gonna finish out some of my automation as well as my task as well. Keith, please, please, you need to make sure that you're reaching out to those parties regarding their late payment.

That's probably the first thing.

That's the point. Yes. Yeah. Yes. Tell me.

Like I said, we're going to be doing a whole lot of more, like I said, AI-based stuff, which honestly, that's the whole thing. That's business in general. We're not focused on just, oh, we're doing AI stuff. No, we're trying to do a complete task with AI. Oh. That's different.

Yeah, let's go ahead and get to it.

Exactly. Exactly. All right, brother. Almost forgot. Well, Let's go ahead and do our thing. I'll talk to you in a bit. Oh, uh...

I almost forgot. This is one part that was pretty important that we pushed off yesterday that we need to make sure we're actually doing today before you actually get into those tasks. So the first thing was to reach out to those parties. The second one, which is pretty important, I need you to go ahead and I got an automation that you can go ahead and create, but you need to do this manually first, and then you can go ahead and do all this other stuff.

I need you to go ahead and give that script That script I gave you.

Script for what?

to AI. Um.

My script?

Yeah, yeah, yeah, I have it on my tasks.

The script so that we can basically go at me. I need you to post 4513 48th Street.

You said a marketplace.

yeah I need you to poke yes so but I need to see whether or not there is a way for I would I would dapper to see if there's a way for a clot to be able to communicate with people off of marketplace I know messenger yes but I'm not sure about marketplace Um...

I think yes, because it comes on messenger as well.

It does, but it's two different places. But if it can, if it can...

do that, then we need to go ahead about training it on responding back. And that's not something I just want to throw together. I want us to work on it. So if you, I think that's probably what you need, because that's something you need to do right now. That's something that you should be working on. That should be your most earliest integration right now. is the that bySpecifically when it comes to speaking to individuals from Facebook Marketplace, From Messenger.

Okay.

if it could be done. Okay, good.

No Messenger, but Facebook Marketplace, yes.

Okay. Okay, so after doing, I mean, after, okay, look, after talking to the tenants who are late, which is my number one priority now,Yeah.

they can post that property at the earliest because they want people to start to respond and then it'll figure out hopefully a way that we can train AI to respond to messages coming back from people on marketplace.

Yes.

Yes.

If that's possible, I'll dig into it. I'll let you know so that you can help me and then we can build it and take it from there.

Okay.

Okay. For sure. A hundred percent.

Yes, that'd be great. Perfect, perfect.

If we can do that, we will be just like... posting marketing and AI is handling the background stuff.

Yeah.

There we go. There we go. Okay. I'll let you go ahead and do your thing.

Let's do it. Very excited. You have no idea. Thanks, man.

And let's go ahead and build this one step at a time, my man. Let's get it. Yeah.

Have a great day, Josh. Thank you. as well.

Talk to you in a bit.
