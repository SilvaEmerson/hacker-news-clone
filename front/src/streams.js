import { webSocket } from "rxjs/webSocket";
import { pluck } from "rxjs/operators";

const buildUrl = (baseUrl, authorName) => `${baseUrl}posts/${authorName}/`;

const url = process.env.REACT_APP_WEBSOCKET_PATH;

export const newPostStream = webSocket(buildUrl(url, "Emerson")).pipe(
  pluck("message", "title")
);
