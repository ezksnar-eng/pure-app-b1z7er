package com.galaxy.airviewdictionary.data.local.vision

import com.galaxy.airviewdictionary.R

enum class TextDetectMode(
    val text: String,
    val iconResourceId: Int,
    val descriptionResourceId: Int,
    val videoResourceId: Int,
) {
    WORD(
        text = "Word detection",
        iconResourceId = R.drawable.ic_detect_mode_word,
        descriptionResourceId = R.string.detect_mode_description_word,
        videoResourceId = R.raw.word_resized_rounded,
    ),
    SENTENCE(
        text = "Sentence detection",
        iconResourceId = R.drawable.ic_detect_mode_sentence,
        descriptionResourceId = R.string.detect_mode_description_sentence,
        videoResourceId = R.raw.sentence_resized_rounded,
    ),
    PARAGRAPH(
        text = "Paragraph detection",
        iconResourceId = R.drawable.ic_detect_mode_paragraph,
        descriptionResourceId = R.string.detect_mode_description_paragraph,
        videoResourceId = R.raw.paragraph_resized_rounded,
    ),
    SELECT(
        text = "Area selection",
        iconResourceId = R.drawable.ic_detect_mode_select,
        descriptionResourceId = R.string.detect_mode_description_select,
        videoResourceId = R.raw.select_resized_rounded,
    ),
    FIXED_AREA(
        text = "Fixed-Area translation",
        iconResourceId = R.drawable.ic_detect_mode_fixedarea,
        descriptionResourceId = R.string.detect_mode_description_fixed_area,
        videoResourceId = R.raw.fixed_area_resized,
    ),
}
