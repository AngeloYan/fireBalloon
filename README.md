# capstone-project-fire-balloon

## User stories
1 story point = 1 hour
Priority range 1 to 5 from highest to lowest.
Epic stories are in bold, followed by their respective user stories.
User stories are formatted as follows: <br>
   As a: <br>
   I want: <br>
   So that: <br>
   Story points: <br>
   Priority: <br>
   Acceptance criteria: <br>

**As a user I want to be able to have questions about a course's outline answered so that I can prepare for the course.**
1. As a: user<br>
   I want: to be able to type messages to the system<br>
   So that: I can request information<br>
   Story points: 4<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - User is able to type in a text box
   - When an on-screen button or the enter key is pressed, the text in the text box is sent to the server
2. As a: user<br>
   I want: my questions and queries about a course outline to be answered<br>
   So that: I can know information relevant to the course<br>
   Story points: 15<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System is able to recognise keywords in question
   - System is able to extract relevant information from a database
   - System is able to display relevant information to the user
   - e.g. who is the lecturer for COMP9900?
   - e.g. tell me the lecturer for COMP9900.
3. As a: user<br>
   I want: the system to recognise my speech<br>
   So that: I can ask my questions out loud<br>
   Story points: 10<br>
   Priority: 2<br>
   Acceptance criteria: <br>
   - When an on-screen button is clicked, the system goes into speech detection mode
   - In speech detection mode, the user cannot enter messages using the keyboard
   - In speech detection mode, the user's speech is converted into text displayed in the text box to enter messages.
   - When the on-screen button is clicked again, the system exits speech detection mode

**As a user I want the system to suggest new questions based on my previous questions so that I save time asking questions.**
1. As a: user<br>
   I want: the sytem to generate questions based on my recent questions<br>
   So that: I save time asking questions<br>
   Story points: 5<br>
   Priority: <br>
   Acceptance criteria: <br>
   - e.g. after answering the question "Who is my lecturer?" the system will suggest the question "What is their email address?"
2. As a: user<br>
   I want: the system's replies to have a conversational flow<br>
   So that: it is intuitive to use<br>
   Story points: 7<br>
   Priority: 3<br>
   Acceptance criteria: <br>
   - System can ask questions for clarification
   - System can ask open ended questions
    - user: tell me about COMP9900<br>
      system: what would you like to know?

**As a user I want the system to answer questions based on the context of the conversation so I can converse with it like I would with a human.**
1. As a: user<br>
   I want: the system to remember information that I have previously given<br>
   So that: I do not have to repeat the information<br>
   Story points: 3<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System stores keywords from previous questions and answers

2. As a: user<br>
   I want: the system to use information that I have previously given to answer my questions<br>
   So that: I do not have to repeat the questions<br>
   Story points: 8<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System uses new information given by the user to generate responses
   - System uses old information given by the user to generate responses

**As a user I want to be able to have questions about a course's content answered so that I can study using the system.**