// IMPORTS
// third-party
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";

// native
import Login from "./Login";


export default function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    <Route path="/" element={<div></div>}></Route>
                    <Route path="/login" element={<Login />}></Route>
                </Routes>
            </Router>
        </div>
    );
}
