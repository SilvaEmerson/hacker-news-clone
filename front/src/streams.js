import { webSocket } from "rxjs/webSocket";
import { pluck } from "rxjs/operators";


export const newPostStream = webSocket('ws://localhost:8000/ws/posts/Emerson/').pipe(pluck('message', 'title'))
