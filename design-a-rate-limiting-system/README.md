<h2>  Design a Rate Limiting System</h2><hr><div><p>A <strong>Rate Limiting System</strong> can allow a maximum of <code>n</code> requests every <code>t</code> seconds, using an implementation similar to <strong>the sliding window algorithm</strong>.</p>

<p>Given two positive integers <code>n</code> and <code>t</code>, and a <strong>non-decreasing</strong> stream of integers representing the timestamps of requests, implement a data structure that can check if each request is allowed or not.</p>

<p>Implement the <strong>RateLimiter</strong> class:</p>

<ul>
	<li><code>RateLimiter(int n, int t)</code> Initializes the RateLimiter object with an empty stream and two integers <code>n</code> and <code>t</code>.</li>
	<li><code>boolean shouldAllow(int timestamp)</code> Returns <code>true</code> if the current request with timestamp <code>timestamp</code> is allowed, otherwise returns <code>false</code>. <strong>Note</strong> that while checking if the current request should be allowed, only the timestamps of requests <strong>previously allowed</strong> are considered.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["RateLimiter", "shouldAllow", "shouldAllow", "shouldAllow", "shouldAllow", "shouldAllow"]
[[3, 5], [1], [1], [2], [3], [8]]
<strong>Output</strong>
[null, true, true, true, false, true]

<strong>Explanation</strong>
RateLimiter rateLimiter = new RateLimiter(3, 5);
rateLimiter.shouldAllow(1); // returns True
                            // There are no previous requests, so this request is allowed.
rateLimiter.shouldAllow(1); // returns True
                            // We can allow 3 requests every 5 seconds, so this request is allowed.
                            // Timestamps of allowed requests are [1,1].
rateLimiter.shouldAllow(2); // returns True
                            // Timestamps of allowed requests are [1,1,2].
rateLimiter.shouldAllow(3); // returns False
                            // This request is not allowed because
                            // the time range [1,3] already has 3 allowed requests.
rateLimiter.shouldAllow(8); // returns True
                            // This request is allowed because
                            // the time range [4,8] does not have any allowed requests.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= t, timestamp&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li>At most <code>10<sup>5</sup></code> calls will be made to <code>shouldAllow</code>.</li>
	<li><code>timestamp</code> values will be <strong>non-decreasing</strong> over all calls made to <code>shouldAllow</code>.</li>
</ul>
</div>