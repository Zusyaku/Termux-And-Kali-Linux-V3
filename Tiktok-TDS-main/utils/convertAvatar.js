let avatarURL = 'https://p16.tiktokcdn.com'

module.exports = (avatar) => {
    avatar = avatar.replace("-sign", "");
    avatar = avatar.replace(/.*tiktokcdn.com/, avatarURL)
    avatar = avatar.replace(/\?.*/,'');

    let avatarWebp = avatar.replace(".jpeg", ".webp");

    return {

        jpeg: {
            //100x100
            small: avatar,

            //300x300
            medium: !avatar.includes("aweme") && avatar.replace("100x100", "300x300") || avatar.replace("100x100", "720x720"), //TikTok doesn't support 300x300 avatars if url contains word "aweme", no clue why

            //720x720
            big: avatar.replace("100x100", "720x720"),

            //1080x1080
            large: avatar.replace("100x100", "1080x1080")
        },

        webp: {

            //100x100
            small: avatarWebp,

            //300x300
            medium: !avatarWebp.includes("aweme") && avatarWebp.replace("100x100", "300x300") || avatarWebp.replace("100x100", "720x720"), //TikTok doesn't support 300x300 avatars if url contains word "aweme", no clue why

            //720x720
            big: avatarWebp.replace("100x100", "720x720"),

            //1080x1080
            large: avatarWebp.replace("100x100", "1080x1080")
        }

    }
}