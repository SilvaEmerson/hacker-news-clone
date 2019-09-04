import React, { useState, useEffect } from "react";
import { newPostStream } from "../streams";

export function NotificationService() {
  const [posts, setPosts] = useState([]);
  const [subscription, setSubscription] = useState(null);

  useEffect(() => {
    const handler = newPost => {
      new Notification(newPost);
      console.log(newPost);
      setPosts(p => [...p, newPost]);
    };

    if (!subscription) {
      let sub = newPostStream.subscribe(handler);
      setSubscription(sub);
    }
  }, [subscription]);

  return (
    <div className="App">
      <h1>Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post}>{post}</li>
        ))}
      </ul>
    </div>
  );
}
