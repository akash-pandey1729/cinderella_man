<h2>  Design Whatsapp</h2><hr><div><p>Design a system like <strong>Whatsapp</strong> with the following features:</p>

<ol>
	<li>Send a <strong>message</strong> to a user.</li>
	<li>Create a <strong>group</strong> with some initial users.</li>
	<li>Add more users to a group.</li>
	<li>Send a message to a group.</li>
	<li>Get messages for a user.</li>
</ol>

<p>Implement the <code>WhatsApp</code> class:</p>

<ul>
	<li><code>WhatsApp()</code> Initializes the object.</li>
	<li><code>void sendMessage(int toUser, String message)</code> Sends a personal message with the text <code>message</code> to the user with id: <code>toUser</code>.</li>
	<li><code>int createGroup(int[] initialUsers)</code> Creates a new group that initially contains users whose ids are in the list <code>initialUsers</code>, and the group id is returned. For each group created, increment the ids <strong>sequentially</strong>. For the first group to be created <code>id = 1</code>, for the second group <code>id = 2</code>, and so on.</li>
	<li><code>void addUserToGroup(int groupId, int userId)</code> Adds the user with id: <code>userId</code> to the group with id: <code>groupId</code>. This call should be <strong>ignored</strong> if the user is already in that group, or if the group does not exist.</li>
	<li><code>void sendGroupMessage(int fromUser, int groupId, String message)</code> Sends a message with the text <code>message</code> by the user with id: <code>fromUser</code> to the group with id: <code>groupId</code>. The message should be sent to all members of the group <strong>except</strong> the sender. Users added afterwards to the group should <strong>not</strong> receive the message. Also, this call should be <strong>ignored</strong> if the user is not a part of the group, or if the group does not exist.</li>
	<li><code>List&lt;String&gt; getMessagesForUser(int userId)</code> Returns all the personal and group messages that were sent to the user with id: <code>userId</code> ordered by the <strong>latest</strong> ones first.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["WhatsApp", "createGroup", "sendMessage", "sendMessage", "getMessagesForUser", "sendGroupMessage", "getMessagesForUser", "addUserToGroup", "sendGroupMessage", "getMessagesForUser", "getMessagesForUser"]
[[], [[1, 2, 3]], [2, "hellotwo"], [4, "hellofour"], [2], [1, 1, "helloeveryone"], [2], [1, 4], [1, 1, "seeyousoon"], [2], [4]]
<strong>Output</strong>
[null, 1, null, null, ["hellotwo"], null, ["helloeveryone", "hellotwo"], null, null, ["seeyousoon", "helloeveryone", "hellotwo"], ["seeyousoon", "hellofour"]]

<strong>Explanation</strong>
WhatsApp whatsApp = new WhatsApp();
whatsApp.createGroup([1, 2, 3]); // return 1
                                 // The first group is created containing the users [1,2,3].
                                 // Since it is the first group, its id will be 1.
whatsApp.sendMessage(2, "hellotwo"); // User 2 receives a personal message "hellotwo".
whatsApp.sendMessage(4, "hellofour"); // User 4 receives a personal message "hellofour".
whatsApp.getMessagesForUser(2); // return ["hellotwo"]
                                // User 2 only received the message "hellotwo" so far.
whatsApp.sendGroupMessage(1, 1, "helloeveryone"); // User 1 sends a message to group 1.
                                                  // So both users 2 and 3 receive the message.
whatsApp.getMessagesForUser(2); // return ["helloeveryone", "hellotwo"]
                                // Two messages were sent to user 2 so far.
whatsApp.addUserToGroup(1, 4); // User 4 is added to group 1.
whatsApp.sendGroupMessage(1, 1, "seeyousoon"); // User 1 sends a message to group 1.
                                               // So users 2, 3, and 4 receive the message.
whatsApp.getMessagesForUser(2); // return ["seeyousoon", "helloeveryone", "hellotwo"]
                                // Three messages were sent to user 2.
whatsApp.getMessagesForUser(4); // return ["seeyousoon", "hellofour"]
                               // Two messages were sent to user 4, so we return them.
                               // Note that user 4 did not receive the message "helloeveryone".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= userId &lt;= 1000</code></li>
	<li><code>1 &lt;= message.length &lt;= 100</code></li>
	<li>The ids in <code>initialUsers</code> are distinct.</li>
	<li>At most <code>100</code> personal messages will be sent to each user.</li>
	<li>At most <code>100</code> groups will be created.</li>
	<li>At most <code>100</code> users will be in each group.</li>
	<li>At most <code>50</code> messages will be sent to each group.</li>
	<li>At most <code>100</code> calls will be made to <code>getMessagesForUser</code>.</li>
	<li><code>message</code> consists of only lowercase English letters.</li>
</ul>
</div>