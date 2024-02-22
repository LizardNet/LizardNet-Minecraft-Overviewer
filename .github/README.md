# LizardNet-Minecraft/Overviewer

> [!IMPORTANT]
> This README is specific to [LizardNet's fork of The Minecraft Overviewer][github] and contains some contextual
> information specifically for this fork. Please read this document carefully before using or contributing to this repo.
>
> For almost all usecases outside LizardNet, we recommend using and contributing to the [upstream project]
> [github-upstream-repo] instead. Because this repo can contain changes intended for internal use, it may not behave as
> expected in other environments. **We make no guarantees or warranties about the suitability of this repo for any
> purpose other than LizardNet's internal use, and we will not provide support for any such use.**

The Minecraft Overviewer is a command-line tool for rendering high-resolution maps of Minecraft (Java Edition) worlds.
It generates a set of static image files and uses LeafletJS to display an interactive map.

This repository is LizardNet's fork of Minecraft Overviewer's [successor project by GregoryAM-SP][github-upstream-repo],
and contains both changes intended to be contributed upstream for the benefit of the community and some changes intended
for internal use. Likewise, we recommend using the [upstream project][github-upstream-repo] for most use cases.

This repository primarily lives in LizardNet Code Review:
- [View repository][gitblit]
- [View Gerrit dashboard][gerrit]

It also is mirrored to GitHub as [LizardNet/LizardNet-Minecraft-Overviewer][github] for convenience. Note that the
mirror is read-only (or, more accurately, unidirectional from Gerrit to GitHub), so changes cannot be directly pushed.
Pull requests are welcome, but need to be copied by an admin to Gerrit after merging.

The `main` branch tracks the upstream project's `main` branch, and the `lizardnet-main` branch contains our changes and
is generally what is used to generate maps for LizardNet's Minecraft servers; for example, the [maps for server s2]
[lizardnet-s2-maps] are generated using this repo's `lizardnet-main` branch, using the configuration in the
[LizardNet-Minecraft-Overviewer-Config][github-config-repo] repo.

> [!NOTE]
> The main README, with general information about Minecraft Overviewer and more information about how to actually use
> this software can be found [in `README.md` in the repo root](/README.md).

[github]: <https://github.com/LizardNet/LizardNet-Minecraft-Overviewer>
[github-upstream-repo]: <https://github.com/GregoryAM-SP/The-Minecraft-Overviewer>
[gitblit]: <https://git.fastlizard4.org/gitblit/summary/?r=LizardNet-Minecraft/Overviewer.git>
[gerrit]: <https://gerrit.fastlizard4.org/r/admin/repos/LizardNet-Minecraft/Overviewer>
[lizardnet-s2-maps]: <https://mcmaps.fastlizard4.org/s2/>
[github-config-repo]: <https://github.com/LizardNet/LizardNet-Minecraft-Overviewer-Config>
