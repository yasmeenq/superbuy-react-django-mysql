

export class ProductModel {
    public id: number = 0;
    public title: string = '';
    public description: string = '';
    public category: string = '';
    public price: number = 0;
    public discountPercentage: number = 0;
    public rating: number = 0;
    public stock: number = 0;
    public tags: string[] = [];
    public brand: string = '';
    public sku: string = '';
    public weight: number = 0;
    public dimensions: { width: number; height: number; depth: number } = { width: 0, height: 0, depth: 0 };
    public warrantyInformation: string = '';
    public shippingInformation: string = '';
    public availabilityStatus: string = '';
    public returnPolicy: string = '';
    public minimumOrderQuantity: number = 1;
    public reviews: { user: string; rating: number; comment: string }[] = [];
    public meta: { createdAt: string; updatedAt: string; barcode: string; qrCode: string } = {
        createdAt: '',
        updatedAt: '',
        barcode: '',
        qrCode: ''
    };
    public images: string[] = [];
    public thumbnail: string = '';
}
