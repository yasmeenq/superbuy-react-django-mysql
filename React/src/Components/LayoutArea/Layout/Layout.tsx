import { Router } from "../../Router/Router";
import { Footer } from "../Footer/Footer";
import { Header } from "../Header/Header";
import css from "./Layout.module.css";

export function Layout(): JSX.Element {
    return (
        <div className={css.Layout}>
			<header>
                <Header />
            </header>

            <main>
                <Router />
            </main>

            <footer>
                <Footer />
            </footer>
        </div>
    );
}
