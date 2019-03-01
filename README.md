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
   Story points: 10<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - User is able to type in a text box
   - When an on-screen button or the enter key is pressed, the text in the text box is sent to the server
2. As a: user<br>
   I want: the system to understand my questions<br>
   So that: the system can provide a relevant answer<br>
   Story points: 20<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System is able to recognise keywords in question
3. As a: user<br>
   I want: the system to respond to my questions with relevant information<br>
   So that: I can know information relevant to the course<br>
   Story points: 30<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System is able to extract relevant information from a database using keywords
   - e.g. who is the lecturer for COMP9900?
   - e.g. tell me the lecturer for COMP9900.
4. As a: user<br>
   I want: the system's answers to be formed into sentences<br>
   So that: it is more natural to converse with the system<br>
   Story points: 20<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System is able to display answers to the user in fully formed sentences
5. As a: user<br>
   I want: the system to recognise my speech<br>
   So that: I can ask my questions out loud<br>
   Story points: 10<br>
   Priority: 2<br>
   Acceptance criteria: <br>
   - When an on-screen button is clicked, the system goes into speech detection mode
   - In speech detection mode, the user cannot enter messages using the keyboard
   - In speech detection mode, the user's speech is converted into text displayed in the text box to enter messages.
   - When the on-screen button is clicked again, the system exits speech detection mode

A large part of the story points in this epic are from the third user story. We are inexperience with Dialogflow, so a large part of this epic will be researching and learning how to use Dialogflow. This user story cannot be broken up into smaller stories because the high number of story points comes from a lack in skills and not the complexity of the story.

**As a user I want the system to be able to respond conversationally so that it is not a simple question and answer bot.**
1. As a: user<br>
   I want: the sytem to suggest new questions based on my recent questions<br>
   So that: I save time asking questions<br>
   Story points: 30<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - The system suggests related questions for the user to ask after it has given an answer
   - e.g. after answering the question "Who is my lecturer?" the system will suggest the question "What is their email address?"
2. As a: user<br>
   I want: the system to ask close ended questions for more information if it cannot answer my question with the given information<br>
   So that: the system can answer my question<br>
   Story points: 30<br>
   Priority: 3<br>
   Acceptance criteria: <br>
   - System can ask close ended questions for clarification
   - e.g. user: tell me about COMP9900<br>
     system: would you like to know about the course outline or course content?
3. As a: user<br>
   I want: the system to ask open ended questions for more information if it cannot answer my question with the given information<br>
   So that: the system can answer my question<br>
   Story points: 30<br>
   Priority: 3<br>
   Acceptance criteria: <br>
   - System can ask open ended questions for clarification
   - e.g. user: tell me about COMP9900<br>
     system: what would you like to know?
4. As a: user<br>
   I want: the system to be able to handle unexpected phrases<br>
   So that: the system can continue the flow of conversation<br>
   Story points: 10<br>
   Priority: 2<br>
   Acceptance criteria: <br>
   - System responds even if unexpected input is given
      - e.g. "daskljfklsadflsa"
5. As a: user<br>
   I want: the system to be able to handle unrelated questions<br>
   So that: the system can continue the flow of conversation<br>
   Story points: 10<br>
   Priority: 2<br>
   Acceptance criteria: <br>
   - System responds even if question unrelated to course outline or content is asked
      - e.g. "What is the weather like?"

**As a user I want the system to answer questions based on the context of the conversation so I can converse with it like I would with a human.**
1. As a: user<br>
   I want: the system to remember information that I have previously given<br>
   So that: I do not have to repeat the information<br>
   Story points: 20<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System stores keywords from previous questions and answers

2. As a: user<br>
   I want: the system to use information that I have previously given to answer my questions<br>
   So that: I do not have to repeat the questions<br>
   Story points: 70<br>
   Priority: 1<br>
   Acceptance criteria: <br>
   - System uses old information given by the user to generate responses

**As a user I want to be able to have questions about a course's content answered so that I can study using the system.**

**As a developer I want it to be easy for users to access the system so that more users will use the system**
1. As a: developer<br>
   I want: users to be able to access the system through Facebook Messenger<br>
   So that: Facebook Messenger will be able to access the system<br>
   Story points: 10<br>
   Priority: 3<br>
   Acceptance criteria: <br>
   - Users can send messages to the system through Facebook Messenger
   - Users can receive messages from the system through Facebook Messenger
2. As a: developer<br>
   I want: users to be able to access the system through Trello<br>
   So that: Trello will be able to access the system<br>
   Story points: 10<br>
   Priority: 4<br>
   Acceptance criteria: <br>
   - Users can send messages to the system through Facebook Messenger
   - Users can receive messages from the system through Facebook Messenger