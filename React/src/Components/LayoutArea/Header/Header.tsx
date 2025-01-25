import { NavLink } from "react-router-dom";
import css from "./Header.module.css";

export function Header(): JSX.Element {
    return (
        <div className={css.Header}>
            <NavLink to={'/products'}>products</NavLink>
        </div>
    );
}
