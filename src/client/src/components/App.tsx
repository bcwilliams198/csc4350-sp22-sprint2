// IMPORTS
// third-party
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

// native
import Login from "./Login";
import { Home } from "./Home";


export default function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    <Route path="/" element={<Home />}></Route>
                    <Route path="/login" element={<Login />}></Route>
                </Routes>
            </Router>
        </div>
    );
}
