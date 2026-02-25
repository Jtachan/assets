# Assets

General assets to be used in different repositories.
Each asset should be called using the following uri:

```
https://raw.githubusercontent.com/Jtachan/assets/refs/heads/main/${PATH_TO_ASSET}
```

I decided to create this repository to avoid adding many images to one repository where I mostly want to keep code.
That way, the load of that repo is smaller.

## Q&A

**Is this created for anyone to use?**

The repository is public and anyone can use it in their own projects.
However, I will maintain the repo considering only the assets I might require.
Anyone is welcome to fork or mirror the repo if they want to do their own modifications.

**[`devicon`](https://github.com/devicons/devicon) already provides icons. Why are you not using them?**

That is true, but I decided to create my own repo for the following reasons:

1. Some icons are not with the style/colors I want. For example, the one provided for Rust.

<table>
    <tr><th>At Devicon</th><th>My asset</th></tr>
    <tr>
      <td><img src=https://raw.githubusercontent.com/devicons/devicon/refs/heads/master/icons/rust/rust-original.svg alt="Rust icon in black"></td>
      <td><img src=./code-icons/rust.svg alt="Rust icon with rusty colors (brown and orange)"></td>
</table>

2. [`devicon`](https://github.com/devicons/devicon) is missing some icons I use, like 'batch.svg' or 'bokeh.svg'.

While I could open tickets there for them to update the repository, they might take a long time to close and the resolution might not always be the one I was looking for.
For those reasons, it is just easier to me to maintain this repo.
