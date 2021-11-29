import praw
import random
import datetime
import time



# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    #"I [THINK] Biden is [SO] [COOL]. He [CAN] do better but it's a [DIFFICULT] role to be in."
    #"Biden was [ELECTED] to be our [PRESIDENT] almost a year ago. That [RACE] was [VERY] [CLOSE]."
    #"Biden likes to [READ] [BOOKS] when he has [FREE] time. Reading is [VALUABLE] and [HELPS] him in many ways.",
    #"Biden is [TALL], [SMART], and [COURAGEOUS]. It's [IMPORTANT] for any president to have these [TRAITS]."
    #"Biden [HATES] eating celery for [DINNER]. He does't think it's [GOOD], he thinks it tastes [WEIRD], and he can only [EAT] it with peanut butter."
    #"Last [SEMESTER], Biden [PRESENTED] his project to my [CLASS]. It was a digital art [PIECE] that he [MADE]."
    
    "[PYTHON] is [SO] [COOL]. It is a [POWERFUL] [SKILL] that everyone can [LEARN].",
    "I [THINK] this [COURSE] is very [USEFUL] for life. I can [ACCOMPLISH] many [THINGS].",
    "I [LIKE] [RIDING] my [BIKE] in the [MORNING]. It makes me feel [GREAT].",
    "I [HATE] eating celery for [DINNER]. It is not [GOOD], it tastes [WEIRD], and I can only [EAT] it with peanut butter.",
    "I [READ] [BOOKS] when I have [FREE] time. Reading is [VALUABLE] and [HELPS] me in many ways.",
    "Last [SEMESTER], I [PRESENTED] my project to my [CLASS]. It was a digital art [PIECE] that I [MADE]."
    ]

replacements = {
    'PYTHON' : ['Python', 'Programming', 'Coding'],
    'SO' : ['so', 'very', 'extremely'],
    'COOL' : ['cool', 'amazing', 'great', 'invigorating'],
    'POWERFUL' : ['powerful', 'valuable', 'mighty', 'wonderful'],
    'SKILL' : ['skill', 'tool'],
    'LEARN' : ['learn', 'master', 'study'],
    'THINK' : ['think', 'believe', 'assume', 'surmise', 'hypothesize'],
    'COURSE' : ['course', 'class'],
    'USEFUL' : ['useful', 'practical', 'beneficial'],
    'ACCOMPLISH' : ['accomplish', 'achieve', 'do'],
    'THINGS' : ['things', 'goals', 'objectives'],
    'LIKE' : ['like', 'enjoy', 'love'],
    'RIDING' : ['riding', 'using', 'fixing', 'steering'],
    'BIKE' : ['bike', 'bicycle', 'scooter', 'unicycle'],
    'MORNING': ['morning', 'afternoon', 'day', 'dorm'],
    'GREAT' : ['great', 'good', 'alright', 'superior'],
    'HATE' : ['hate', 'dislike', 'detest'],
    'DINNER' : ['dinner', 'breakfast', 'lunch', 'brunch'],
    'GOOD' : ['good', 'delicious', 'tasty', 'appetizing', 'delectable'],
    'WEIRD' : ['weird', 'disgusting', 'nasty', 'bad', 'awful'],
    'EAT' : ['eat', 'consume', 'devour', 'chew'],
    'READ' : ['read', 'skim', 'peruse', 'see'],
    'BOOKS' : ['books', 'articles', 'journals', 'autobiographies'],
    'FREE' : ['free', 'extra', 'more', 'leisure'],
    'VALUABLE' : ['valuable', 'powerful', 'important', 'useful'],
    'HELPS' : ['helps', 'assists', 'aids'],
    'SEMESTER' : ['semester', 'year'],
    'PRESENTED' : ['presented', 'showed', 'displayed'],
    'CLASS' : ['class', 'classmates', 'peers', 'professor'],
    'PIECE' : ['piece', 'drawing', 'painting', 'portrait'],
    'MADE' : ['made', 'created', 'produced', 'designed'],
    #'CAN' : ['can', 'should', 'must'],
    #'DIFFICULT' : ['difficult', 'challenging', 'hard', 'tough'],
    #'ELECTED' : ['elected', 'chosen', 'picked'],
    #'PRESIDENT' : ['president', 'leader', 'general', 'officer'],
    #'RACE' : ['race', 'election', 'competition'],
    #'VERY' : ['very', 'extremely', 'somewhat', 'especially'],
    #'CLOSE' : ['close', 'tight', 'tense'],
    #'TALL' : ['tall', 'short', 'skinny'],
    #'SMART' : ['smart', 'intelligent', 'cunning'],
    #'COURAGEOUS' : ['courageous', 'brave', 'valiant', 'bold'],
    #'IMPORTANT' : ['important', 'essential', 'crucial', 'necessary'],
    #'TRAITS' : ['traits', 'characteristics', 'attributes']

    }

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''

    #random_string = madlibs.random.choice()
    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('['+k+']', random.choice(replacements[k]))
    return s

# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot', user_agent='cs40bot')

# FIXME:
# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
#submission_url = 'https://old.reddit.com/r/BotTown/comments/qzdy2o/submission/?' # CHANGE TO MAIN DISCUSSION THREAD
#submission = reddit.submission(url=submission_url)
submission = reddit.submission('r0yi9l')

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True: 

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments: 
        if str(comment.author) != 'compsci40-bot':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)
    
    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)
        

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            if comment.author != 'compsci40-bot':
                result = False
                for reply in comment.replies:
                    if str(reply.author) =='compsci40-bot':
                        result = True
                if result is False:
                    comments_without_replies.append(comment)
        print(len(comments_without_replies))
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        comment = random.choice(comments_without_replies)
        try:
            comment.reply(generate_comment())
        except praw.exceptions.APIException:
            print('No reply to deleted comment')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    fivehotsubmissions = []
    for submission in reddit.subreddit("BotTown2").hot(limit=5):
        fivehotsubmissions.append(submission)
    n_submission = random.choice(fivehotsubmissions)
    submission = reddit.submission(id=n_submission)
    #print('submission id:', n_submission)
    #print(n_submission.title)
    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(2)
