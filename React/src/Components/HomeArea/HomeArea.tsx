import toast from "react-hot-toast";
import css from "./HomeArea.module.css";

export function HomeArea(): JSX.Element {

    function showSuccess(){
        toast.success('this is success');
    }
    function showError(){
        toast.error('this is error');
    }

    return (
        <div className={css.HomeArea}>
			<button onClick={showSuccess}>Success</button>
            <button onClick={showError}>Error</button>
        </div>
    );
}
