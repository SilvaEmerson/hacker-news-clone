import React, { useState, useEffect } from "react";
import "./App.css";
import { newPostStream } from "./streams";

export const App = () => {
  const [posts, setPosts] = useState([]);
  const [notficationStatus, setNotficationStatus] = useState("denied");

  useEffect(() => {
    newPostStream.subscribe(post => {
      console.log(post);
      if (notficationStatus !== "denied") new Notification(post);
      setPosts([...posts, post]);
    });

    Notification.requestPermission(function(status) {
      console.log("Notification permission status:", status);
      setNotficationStatus(status);
    });
  }, [posts, notficationStatus]);

  return (
    <div className="App">
      <ul>
        {posts.map(post => (
          <li key="{post}">{post}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
