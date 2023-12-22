# Marpit Cheat Sheet

## Marpit
- Introduction
- Usage

## Marpit Markdown
- Directives
- Image syntax
- Resizing image
- Image filters
- Slide backgrounds
- Background size
- Advanced backgrounds
  - Multiple backgrounds
  - Split backgrounds
- Fragmented list
- Theme CSS
- Inline SVG slide

## Marpit API
- [Marpit API (JSDoc)](https://github.com/marp-team/marp)

## GitHub and npm
- [GitHub Repository](https://github.com/marp-team/marp)
- [npm Package](https://www.npmjs.com/package/marp)

## Note
- This documentation is targeted for JavaScript developers using the Marpit framework.
- If you are a consumer of Marp and not familiar with engineering, it may be challenging to understand the contents.

## Image syntax
Marpit extends Markdown image syntax `![](image.jpg)` for creating beautiful slides.

### Features
|                   | Inline image | Slide BG | Advanced BG |
|-------------------|--------------|----------|-------------|
| Resizing keywords | auto only     | ✔️       | ✔️          |
| Resizing %        | ❌            | ✔️       | ✔️          |
| Resizing length   | ✔️           | ✔️       | ✔️          |
| Image filters     | ✔️           | ❌       | ✔️          |
| Multiple BGs      | ❌            | ✔️       | ✔️          |
| Split BGs         | ❌            | ✔️       | ✔️          |

### Resizing image
- Use width and height keywords:
  - `![width:200px](image.jpg)` <!-- Setting width to 200px -->
  - `![height:30cm](image.jpg)` <!-- Setting height to 300px -->
  - `![width:200px height:30cm](image.jpg)` <!-- Setting both lengths -->
- Shorthand options:
  - `![w:32 h:32](image.jpg)` <!-- Setting size to 32x32 px -->

### Image filters
- Apply CSS filters through markdown image syntax:
  - `![blur:10px]()`
  - `![brightness:1.5]()`
  - ...

### Slide backgrounds
- Specify slide background through Markdown:
  - `![bg](https://example.com/background.jpg)`

### Background size
- Resize background image by keywords:
  - `![bg contain](https://example.com/background.jpg)`
- Keyword values:
  - cover, contain, fit, auto, x%
  - `![bg 150%](image.jpg)`

### Advanced backgrounds
- Experimental inline SVG slide.
- Support multiple backgrounds, split backgrounds, and image filters.

#### Multiple backgrounds
- Horizontal arrangement:
  - `![bg](https://fakeimg.pl/800x600/0288d1/fff/?text=A)`
  - `![bg](https://fakeimg.pl/800x600/02669d/fff/?text=B)`
  - `![bg](https://fakeimg.pl/800x600/67b8e3/fff/?text=C)`

#### Split backgrounds
- Shrink slide content space:
  - `![bg left](https://picsum.photos/720?image=29)`

#### Split size
- Specify split size by percentage:
  - `![bg left:33%](https://picsum.photos/720?image=27)`

### GitHub and npm
- [GitHub Repository](https://github.com/marp-team/marp)
- [npm Package](https://www.npmjs.com/package/marp)


https://marpit.marp.app/image-syntax