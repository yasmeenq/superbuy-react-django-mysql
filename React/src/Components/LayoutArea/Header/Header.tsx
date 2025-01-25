import { NavLink } from "react-router-dom";
import css from "./Header.module.css";
import storeLogo from "../../../assets/images/storeLogo.jpg";

export function Header(): JSX.Element {
    return (
        <div className={css.Header}>
            <div className={css.navLeft}>
                <img className={css.Logo} src={storeLogo} alt='storeLogo' />
            </div>

            <div className={css.navMiddle}>
                <NavLink to={'/products'}>products   | </NavLink>
                <NavLink to={'/home'}>home</NavLink>
            </div>
            <div className={css.navRight}></div>

        </div>
    );
}
