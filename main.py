from flask import Flask, jsonify, request
from model_loader import load_model, predict_inflation
import os

app = Flask(__name__)

# dummy nya MD
commodities = [
    {"id": 1, "title": "Ayam Negri", "img": "https://cdn.peternak.id/images/peternak-ayam-potong-1160x680.jpg"},
    {"id": 2, "title": "Cabe Merah", "img": "https://storage.googleapis.com/bucket-model-daerah/06bb004d-816b-40b6-97ce-22d9a00e6629.jpg"}
]

provinces = [
    {"id": 1, "name": "Jawa Barat", "image": "https://storage.googleapis.com/bucket-model-daerah/images.png"},
    {"id": 2, "name": "Jawa Timur", "image": "https://storage.googleapis.com/bucket-model-daerah/images%20(1).png"}
]

@app.route('/commodities', methods=['GET'])
def get_commodities():
    return jsonify({"error": False, "message": "success", "listCommodities": commodities})

@app.route('/commodities/<int:commodity_id>/provinces', methods=['GET'])
def get_provinces(commodity_id):
    return jsonify({"error": False, "message": "success", "listProvinces": provinces})

@app.route('/commodities/<int:commodity_id>/provinces/<int:province_id>/inflation-predictions', methods=['GET'])
def get_inflation_predictions(commodity_id, province_id):
    # modelnya use based on commodity_id
    model_name = f"model{commodity_id}"
    
    try:
        time_range = int(request.args.get('timeRange', 30))
        model = load_model(model_name)
        predictions = predict_inflation(model, time_range)
        return jsonify({
            "error": False,
            "message": "success",
            "predictions": predictions,
            "description": f"Inflation predictions for commodity {commodity_id} in province {province_id}."
        })
    except ValueError as e:
        return jsonify({"error": True, "message": str(e)}), 400

@app.route('/commodities/<int:commodity_id>/provinces/<int:province_id>/normal-prices', methods=['GET'])
def get_normal_prices(commodity_id, province_id):
    # dummy harga
    prices = [{"date": "2024-01", "value": 150000}, {"date": "2024-02", "value": 155000}]
    return jsonify({
        "error": False,
        "message": "success",
        "prices": prices,
        "description": f"Normal prices for commodity {commodity_id} in province {province_id}."
    })

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    results = [
        {"id": 1, "type": "commodity", "name": "Beras", "image": "https://example.com/beras.jpg"},
        {"id": 2, "type": "province", "name": "Jawa Barat", "image": "https://example.com/jawa_barat.jpg"}
    ]
    filtered_results = [r for r in results if query.lower() in r['name'].lower()]
    return jsonify({"error": False, "message": "success", "results": filtered_results})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
