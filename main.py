from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Menú Digital Gastronómico")

# Habilitar CORS para conectar con el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base de datos ampliada con más categorías y productos
PRODUCTS_DB = [
    # 🔥 Más Vendidas
    {
        'id': '1',
        'category': '🔥 Más Vendidas',
        'name': 'Hamburguesa Fuego Gourmet',
        'desc': '150g carne angus, queso cheddar fundido, cebolla caramelizada, pan brioche.',
        'price': 26000,
        'image': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500'
    },
    {
        'id': '2',
        'category': '🔥 Más Vendidas',
        'name': 'Volcán de Tocineta',
        'desc': 'Doble carne angus, queso ahumado, mermelada de tocineta y salsa BBQ ahumada.',
        'price': 29500,
        'image': 'https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=500'
    },
    # 🍔 Hamburguesas
    {
        'id': '3',
        'category': '🍔 Hamburguesas',
        'name': 'Combo Doble Carbón',
        'desc': 'Doble carne 150g, doble queso, tocineta crujiente, papas y bebida.',
        'price': 34000,
        'image': 'https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=500'
    },
    {
        'id': '4',
        'category': '🍔 Hamburguesas',
        'name': 'Crispy Chicken Supreme',
        'desc': 'Pechuga crujiente estilo sureño, ensalada coleslaw, pepinillos y mayonesa spicy.',
        'price': 24900,
        'image': 'https://images.unsplash.com/photo-1625813506062-0aeb1d7a094b?w=500'
    },
    {
        'id': '5',
        'category': '🍔 Hamburguesas',
        'name': 'Veggie Portobello',
        'desc': 'Hongo Portobello a la parrilla, queso de cabra, rúcula fresca y pesto de tomates.',
        'price': 25500,
        'image': 'https://images.unsplash.com/photo-1525059696034-4967a8e1dca2?w=500'
    },
    # 🍟 Acompañamientos
    {
        'id': '6',
        'category': '🍟 Acompañamientos',
        'name': 'Papas Rústicas Trufadas',
        'desc': 'Corte rústico con aceite de trufa blanca, queso parmesano y perejil fresco.',
        'price': 14000,
        'image': 'https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=500'
    },
    {
        'id': '7',
        'category': '🍟 Acompañamientos',
        'name': 'Aros de Cebolla Artesanales',
        'desc': 'Crujientes aros de cebolla apanados acompañados de salsa tártara de la casa.',
        'price': 12000,
        'image': 'https://images.unsplash.com/photo-1639024471283-03518883512d?w=500'
    },
    {
        'id': '8',
        'category': '🍟 Acompañamientos',
        'name': 'Nachos Tex-Mex',
        'desc': 'Totopos crocantes con guacamole casero, chili con carne y queso cheddar fluido.',
        'price': 19000,
        'image': 'https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?w=500'
    },
    # 🥤 Bebidas
    {
        'id': '9',
        'category': '🥤 Bebidas',
        'name': 'Limonada de Coco Artesanal',
        'desc': 'Limonada natural recién exprimida batida con crema de coco gourmet (400ml).',
        'price': 9000,
        'image': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=500'
    },
    {
        'id': '10',
        'category': '🥤 Bebidas',
        'name': 'Malteada Red Velvet',
        'desc': 'Helado artesanal de vainilla con trozos de pastel red velvet y crema batida.',
        'price': 13500,
        'image': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=500'
    },
    {
        'id': '11',
        'category': '🥤 Bebidas',
        'name': 'Cerveza IPA Artesanal',
        'desc': 'Cerveza rubia de la casa con notas cítricas e intensas (330ml).',
        'price': 11000,
        'image': 'https://images.unsplash.com/photo-1608270586620-248524c67de9?w=500'
    },
    {
        'id': '12',
        'category': '🥤 Bebidas',
        'name': 'Soda Frutos Rojos',
        'desc': 'Soda italiana infusionada con mora, frambuesa, arándanos y menta fresca.',
        'price': 8500,
        'image': 'https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=500'
    }
]

@app.get("/api/products")
def get_products():
    return PRODUCTS_DB