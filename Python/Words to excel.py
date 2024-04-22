import pandas as pd

input_string = """CLEANING

Dish soap

Laundry detergent

All-purpose cleaner

Hand soap

Broom

Mop

Wash cloths/rags

Vacuum

Dustpan

Lint roller

Sponges

KITCHENWARE

• Plates

Bowls

Spoons

Forks

Knives

Glasses

Mugs

Tongs

Spatula

Plastic wrap

Ziplock baggies

Garbage bags

Paper towel

Tupperware

Ice tray

Oven mitts

Potato peeler

Mixing bowls

Frying pan

Pot

Baking sheet

Whisk

Stirring spoons/ladels

Tea infuser ball

Measuring cups

Strainer

Cutting board

Coffee maker

Kettle

Toaster

Magnets

Dry erase markers.

Sticky notes

Microwave

Wire sponge

Trash bin

Recycling bin

Rubber gloves

Silverware organizer

Measuring spoons

Aluminum foil

Wax paper

Can opener

Bottle opener

Containers for salt, sugar, flour, etc.

LIVINGROOM

Sofa

Rocking chair (you know you want one)

Loveseat

Coasters

Blankets

Throw pillows

Coffee table

Book shelves

TV

TV stand

Floor lamp

End table

• Stereo system/radio

BEDROOM

Mattress

Box spring

Bedframe

Linens

Sheets

Comforter

Hangers

Laundry hamper

Trash bin

Curtains

Pillows

Pillow cases

Night table

Alarm clock

Lamp

Dresser

Coat rack

Desk/vanity

• Comfy chairs

DININGROOM

Dining table

Minimum of 2 chairs

Coasters

Placemat

Tablecloth

Tea lights /candles and candle holders

BATHROOM

Face clothes

Towel

Soap bar

Body wash

Shampoo

Conditioner

Tissues

Toilet paper

Trash bin

Plunger

Toilet cleaner

Cold, flu, pain, and allergy meds

Hydrogen peroxide

Antibacterial ointment

First-Aid kit

Tweezers

Nail clippers

Band-aids

Shower rad

Shower curtain

Toothbrush

Toothpaste

Floss

Period products

Bathmat

Air freshener

Trash bin

Towel rod

Towels

MISCELLANEOUS

Elastic bands

Stapler

Stables

Paper clips

Needles and thread

AA/AAA batteries

Light bulbs.

Extension cords.

Scotch tape

Duct tape

Shovel

Rake (if you have a yard)

Stain remover

Jar of courters for laundry mat

Screw drivers

Hammer

Nails

Sticky tack

Screws

Box cutter/X-acto

Pliers

Wrench

Pens

Paper

Pencils

Pencil sharpener

Eraser

Welcome matt

Shoe rack

Coat rack

Flashlight

Flashlight batteries

Watch batteries

Rechargeable batteries and charger

Safe place to discard dead batteries

Candies

Matches

Lighter

Mini travel fans

Real fans

Emergency Survival kit

Fire extinguisher

Landline phone

Window air conditioner

Carbon monoxide alarm

• Fire alarm

FOOD STUFF

Mustard

Ketchup

Mayo

Salt

Pepper

Baking soda

Flour

Eggs

Milk

Bread

Olive oil

Tea

Jam

Peanut-butter

Coffee grounds

Cereal

Rice

Pasta

Vegetable soup

Tomato sauce

Frozen vegetables

Crackers

Chickpeas/lentils

Apples

Oranges

Granola bars

Juice

Hot chocolate mix

Frozen meats"""

# Split the input string by newline character
words = input_string.split('\n')

# Create a DataFrame from the words list
df = pd.DataFrame(words, columns=['Words'])

df.to_excel('essestial_items.xlsx', index=False)

print("Excel file created successfully.")