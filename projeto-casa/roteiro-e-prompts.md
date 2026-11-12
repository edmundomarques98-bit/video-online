# Casa — roteiro e prompts (estilo "ambientação 3D")

Referência: reel com passeio pela casa, os móveis aparecendo cômodo por cômodo.
Formato final: **9:16 (1080×1920)**, com cerca de 55 a 65 s.

Fotos de cada cena: pasta `fotos/` (o número no nome é o número da cena).
Mapa visual das cenas: `mapa-cenas.jpg`.

---

## Como usar (3 passos por cena)

**Passo A: verticalizar (Gemini / Nano Banana)**
Anexa a foto da cena e cola o prompt A. Ele é o mesmo pra todas as cenas.
O resultado é o **QUADRO VAZIO** em 9:16.

**Passo B: render (Gemini / Nano Banana)**
Anexa o QUADRO VAZIO (resultado do passo A) e cola o prompt B da cena.
O resultado é o **RENDER**.

**Passo C: transformação (Veo 3, no Flow)**
Usa o modo *Frames to Video*: quadro inicial = QUADRO VAZIO, quadro final = RENDER.
Formato **9:16**. Cola o prompt C da cena. Pode ignorar o áudio que o Veo gera.

Me devolve três arquivos por cena: o QUADRO VAZIO, o RENDER e o vídeo do Veo.
Nomeia assim: `cena04-vazio.jpg`, `cena04-render.jpg`, `cena04-veo.mp4`.

> Confere o render antes de ir pro Veo: as portas, as janelas, o piso e as paredes precisam continuar iguais à casa real. Se a IA mudar a arquitetura, gera de novo.

---

## PROMPT A — verticalizar (igual pra todas as cenas)

```
Recreate this exact photo as a vertical 9:16 image. Same place, same camera position, same perspective and lens. Keep every wall, door, window, floor tile, ceiling, texture, color and light exactly as in the photo, including the construction mess on the floor. Extend the image naturally at the top and bottom so the full room fits the vertical frame. Do not add or remove anything. Photorealistic, looks like a real smartphone photo.
```

---

## Estilo base dos renders (já está dentro de cada prompt B)
Segue a referência: madeira freijó, preto fosco, tecidos cinza chumbo e bege, luz quente de LED junto com a luz do dia, render fotorrealista.

---

## CENA 1 — Fachada · foto `cena01-fachada.jpg`
No vídeo, a logo entra grande e depois vira marca d'água. Essa parte eu faço na edição.

**B (render)**
```
Use this image as the base. Same camera, same composition. Keep the white garage gate, the dark gray marble panel, the two black vertical columns, the meter boxes and the concrete ramp exactly as they are. Add: tall slim tropical plants in black planters at both sides of the ramp, warm recessed spotlights under the top slab turned on, warm wall washers glowing on the marble panel, clean swept ground with no litter. Late afternoon golden sunlight, blue sky with soft white clouds. Photorealistic architectural photo, high detail, vertical 9:16.
```
**C (Veo)**
```
Vertical shot, very slow push-in toward the house. The litter on the ground disappears, black planters rise from the ground at both sides of the ramp and plants grow in seconds, the ceiling spotlights and wall lights switch on one by one, sunlight turns warm golden. Ends exactly on the final frame. Photorealistic, smooth, satisfying. No people, no text.
```

---

## CENA 2 — Frente / garagem · foto `cena02-frente-garagem.jpg`

**B (render)**
```
Use this image as the base. Same camera, same composition. Keep the gray textured walls, the tile roof, the covered porch, the small horizontal window, the glass entrance door with black handles, the concrete slab path with gravel and the black wall lights exactly as they are. Remove the ladder, the trash bag and the blue hose. Add: a modern dark gray SUV parked on the concrete slab tracks, a freijó wood slatted panel on the back wall of the covered porch, two lounge chairs with gray cushions and a small side table under the porch, large tropical plants in black pots along the left wall, warm wall lights turned on. Golden hour sunlight, blue sky with clouds. Photorealistic, vertical 9:16.
```
**C (Veo)**
```
Static vertical shot, camera slowly pushes forward. The ladder, the trash bag and the hose vanish, a dark gray SUV rolls in from the bottom of the frame and parks on the slab tracks, wood slats slide onto the porch back wall one by one, lounge chairs and potted plants drop from above and land softly, wall lights switch on. Ends exactly on the final frame. Photorealistic, smooth. No people, no text.
```

---

## CENA 3 — Chuveirão · foto `cena03-chuveirao.jpg`

**B (render)**
```
Use this image as the base. Same camera, same composition. Keep the wood-look porcelain wall, the black rain shower head, the shower tray, the gray textured walls, the gravel and the stone slabs exactly as they are. Remove the blue hose. Add: lush tropical plants (palms and monstera) in black planters on both sides of the shower, a freijó wood bench with rolled white towels, a warm LED uplight glowing on the wood wall, a few round river stones around the tray. Golden hour sunlight, blue sky. Photorealistic, vertical 9:16.
```
**C (Veo)**
```
Static vertical shot. The hose slides away and disappears, the rain shower turns on and water starts falling, plants sprout from the gravel and grow fast on both sides, a wooden bench with towels appears, the uplight switches on the wood wall. Ends exactly on the final frame. Photorealistic, smooth, satisfying. No people, no text.
```

---

## CENA 4 — Sala · foto `cena04-sala.jpg` (entrando pela porta de vidro)

**B (render)**
```
Use this image as the base. Same camera, same composition, the glass doors with black handles stay in the foreground. Keep the marble-look porcelain floor, the cream walls, the wooden louvered door on the back wall and the corridor opening exactly as they are. Remove the red cloth from the floor. Add: on the right wall a dark gray 3-seat sofa with beige cushions and a large abstract framed painting above it; on the left side a freijó wood slatted TV panel with a floating rack and a TV; a geometric beige and gray rug; a wooden coffee table; a tall plant in a black pot in the corner; black ceiling track lights with warm spots turned on. Natural daylight plus warm LED accents. Photorealistic interior render, vertical 9:16.
```
**C (Veo)**
```
Vertical shot, camera slowly pushes in through the open glass doors. The red cloth disappears, wood slats of the TV panel slide onto the wall one by one, the rug unrolls across the floor, the sofa drops from the ceiling and bounces softly onto it, coffee table and plant pop in, ceiling track lights switch on. Ends exactly on the final frame. Photorealistic, smooth, satisfying. No people, no text.
```

---

## CENA 5 — Cozinha · foto `cena05-cozinha.jpg`

**B (render)**
```
Use this image as the base. Same camera, same composition. Keep the black granite countertop with the sink and the black gourmet faucet, the horizontal window, the marble-look wall tiles and the floor exactly as they are. Remove the small objects on the countertop. Add: under-counter cabinets in matte charcoal gray with a freijó wood handle strip, freijó wood upper cabinets beside the window without covering it, warm LED strip under the upper cabinets, a built-in black cooktop on the counter, a stainless steel fridge on the right side, a coffee machine, a fruit bowl and a small plant. Warm lighting plus daylight from the window. Photorealistic interior render, vertical 9:16.
```
**C (Veo)**
```
Static vertical shot, slow push-in. The kitchen assembles itself: cardboard boxes fly in and burst open, cabinet doors fly out of them and snap into place under the counter, upper cabinets slide onto the wall, the fridge rises out of a box, the cooktop drops into the counter, LED strips switch on under the cabinets. Ends exactly on the final frame. Photorealistic, smooth, satisfying. No people, no text.
```

---

## CENA 6 — Quarto 1 · foto `cena06-quarto1.jpg`

**B (render)**
```
Use this image as the base. Same camera, same composition, the wooden door stays in the foreground. Keep the window, the switches and outlets, the cream walls and the marble-look floor exactly as they are. Add: a queen bed with a tall upholstered beige headboard against the right wall, gray and white bedding with a knitted throw, two freijó wood nightstands with warm lamps turned on, a soft gray rug, linen curtains on the window, two framed abstract prints above the headboard, a small plant. Cozy warm lighting plus daylight. Photorealistic interior render, vertical 9:16.
```
**C (Veo)**
```
Static vertical shot. A rolled mattress drops onto the floor and unfolds into a full bed, the headboard slides up the wall, nightstands pop in and the lamps switch on, the rug unrolls, curtains unroll over the window, frames appear on the wall. Ends exactly on the final frame. Photorealistic, smooth, satisfying. No people, no text.
```

---

## CENA 7 — Banheiro · foto `cena07-banheiro.jpg`

**B (render)**
```
Use this image as the base. Same camera, same composition, the wooden door frames stay in the foreground. Keep the marble-look porcelain walls, the two small high windows, the countertop shape and the floor exactly as they are. Remove all boxes, packaging and debris. Add: a white countertop sink with a black faucet, a freijó wood vanity cabinet under the counter, a large round backlit mirror above the counter, a frameless glass shower enclosure with black profile and a black rain shower in the back, a lit niche in the shower wall, white towels, a small plant, warm LED cove light on the ceiling. Photorealistic interior render, vertical 9:16.
```
**C (Veo)**
```
Static vertical shot. The boxes and debris on the counter burst into dust and vanish, the vanity cabinet assembles under the counter, the sink and faucet drop into place, the round mirror appears and lights up, the glass shower panel slides in, towels and plant pop in, ceiling LED switches on. Ends exactly on the final frame. Photorealistic, smooth, satisfying. No people, no text.
```

---

## CENA 8 — Quarto 2 · `cena08-quarto2-frame-video.jpg` (quadro tirado do vídeo)
⚠️ Esse quadro tem qualidade baixa porque o vídeo veio comprimido pelo WhatsApp. Se tiver uma foto desse quarto, usa ela no lugar.

**B (render)**
```
Use this image as the base. Same camera, same composition. Keep the window, the cream walls, the switches and the marble-look floor exactly as they are. Add: a double bed with a gray upholstered headboard, beige and white bedding, a freijó wood desk with a black chair under the window, a floating shelf with books and plants, a soft rug, sheer curtains, a pendant lamp turned on. Warm lighting plus daylight. Photorealistic interior render, sharp and high detail, vertical 9:16.
```
**C (Veo)**
```
Static vertical shot. The bed drops softly from the ceiling, the headboard slides up the wall, the desk and chair pop in under the window, books and plants jump onto the shelf, curtains unroll, the pendant lamp switches on. Ends exactly on the final frame. Photorealistic, smooth, satisfying. No people, no text.
```

---

## CENA 9 — Lavanderia · foto `cena09-lavanderia.jpg` (opcional)

**B (render)**
```
Use this image as the base. Same camera, same composition. Keep the gray textured walls, the marble-look backsplash with two faucets, the sink counter and the door to the kitchen exactly as they are. Remove the broom, bottles, bucket, red cloth, wooden stick and debris. Add: a white front-load washing machine next to the sink, a wall-mounted charcoal gray cabinet above it, woven baskets, a foldable drying rack, a small plant, clean floor. Natural light. Photorealistic, vertical 9:16.
```
**C (Veo)**
```
Static vertical shot. The broom, bucket, bottles and cloth fly away and vanish, the washing machine slides in from the side, the cabinet drops onto the wall, baskets and plant pop in. Ends exactly on the final frame. Photorealistic, smooth. No people, no text.
```

---

## CENA 10 — Fundos → área gourmet · foto `cena10-fundos.jpg` (final do vídeo)
Atenção: a churrasqueira e o deck são **sugestão de ambientação**. Confirma com o cliente antes de publicar, pra ninguém achar que a casa já vem com eles.

**B (render)**
```
Use this image as the base. Same camera, same composition. Keep the gray textured walls, the window and the roof edge exactly as they are. Add: a wooden deck floor, a black pre-molded barbecue grill against the back wall, a small black granite counter beside it, a wooden table with four chairs, potted tropical plants, a vertical garden on the left wall, warm string lights stretched across the walls and turned on. Golden hour sunlight, blue sky. Photorealistic, vertical 9:16.
```
**C (Veo)**
```
Static vertical shot. Wooden deck planks slide across the floor one by one, a black barbecue grill drops from the sky and lands against the back wall, table and chairs pop up, plants grow, string lights stretch across and switch on one by one. Ends exactly on the final frame. Photorealistic, smooth, satisfying. No people, no text.
```

---

## O que eu faço na edição
- Passeio real entre as cenas, com trechos do vídeo bruto (fachada → jardim → sala → cozinha → corredor → quartos → banheiro).
- Logo grande na abertura, depois vira marca d'água fixa embaixo.
- Corte dos clipes do Veo pra 4–5 s, segurando o render 1–2 s.
- Música (você manda, ou deixo a faixa livre).

## Pendências
- [ ] Vídeo/fotos em qualidade original (sem compressão do WhatsApp)
- [ ] Logo do cliente (PNG transparente) e texto da marca d'água (WhatsApp/@)
- [ ] Confirmar a mobília (se o cliente tiver preferência)
- [ ] Confirmar a churrasqueira/deck da cena 10
