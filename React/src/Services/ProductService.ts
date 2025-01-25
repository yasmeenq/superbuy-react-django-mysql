import axios from "axios";
import { ProductModel } from "../Models/ProductModel";
import { appConfig } from "../Utils/AppConfig";
import toast from "react-hot-toast";


class ProductService {

	public async getAllProducts(): Promise<ProductModel[]> {
        const response = await axios.get<ProductModel[]>(appConfig.productsURL);
        const dbProducts = response.data;
        toast.success('products fetched from DB successfully!');
        return dbProducts;
    }
}

export const productService = new ProductService();
