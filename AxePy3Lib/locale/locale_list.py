#!/usr/bin/env python3
#
# Copyright 2007 Doug Hellmann.
#
"""Print a list of locale codes and location names.

This information was cut from the Python 3.5.1 version of
locale.py, and reformatted to move the place names out of
comments into text which could be printed by the script.

"""

#end_pymotw_header

locales = [
    ("af_ZA", "Afrikaans"),
    ("sq_AL", "Albanian"),
    ("gsw_FR", "Alsatian - France"),
    ("am_ET", "Amharic - Ethiopia"),
    ("ar_SA", "Arabic - Saudi Arabia"),
    ("ar_IQ", "Arabic - Iraq"),
    ("ar_EG", "Arabic - Egypt"),
    ("ar_LY", "Arabic - Libya"),
    ("ar_DZ", "Arabic - Algeria"),
    ("ar_MA", "Arabic - Morocco"),
    ("ar_TN", "Arabic - Tunisia"),
    ("ar_OM", "Arabic - Oman"),
    ("ar_YE", "Arabic - Yemen"),
    ("ar_SY", "Arabic - Syria"),
    ("ar_JO", "Arabic - Jordan"),
    ("ar_LB", "Arabic - Lebanon"),
    ("ar_KW", "Arabic - Kuwait"),
    ("ar_AE", "Arabic - United Arab Emirates"),
    ("ar_BH", "Arabic - Bahrain"),
    ("ar_QA", "Arabic - Qatar"),
    ("hy_AM", "Armenian"),
    ("as_IN", "Assamese - India"),
    ("az_AZ", "Azeri - Latin"),
    ("az_AZ", "Azeri - Cyrillic"),
    ("ba_RU", "Bashkir"),
    ("eu_ES", "Basque - Russia"),
    ("be_BY", "Belarusian"),
    ("bn_IN", "Begali"),
    ("bs_BA", "Bosnian - Cyrillic"),
    ("bs_BA", "Bosnian - Latin"),
    ("br_FR", "Breton - France"),
    ("bg_BG", "Bulgarian"),
    ("ca_ES", "Catalan"),
    ("zh_CHS", "Chinese - Simplified"),
    ("zh_TW", "Chinese - Taiwan"),
    ("zh_CN", "Chinese - PRC"),
    ("zh_HK", "Chinese - Hong Kong S.A.R."),
    ("zh_SG", "Chinese - Singapore"),
    ("zh_MO", "Chinese - Macao S.A.R."),
    ("zh_CHT", "Chinese - Traditional"),
    ("co_FR", "Corsican - France"),
    ("hr_HR", "Croatian"),
    ("hr_BA", "Croatian - Bosnia"),
    ("cs_CZ", "Czech"),
    ("da_DK", "Danish"),
    ("gbz_AF", "Dari - Afghanistan"),
    ("div_MV", "Divehi - Maldives"),
    ("nl_NL", "Dutch - The Netherlands"),
    ("nl_BE", "Dutch - Belgium"),
    ("en_US", "English - United States"),
    ("en_GB", "English - United Kingdom"),
    ("en_AU", "English - Australia"),
    ("en_CA", "English - Canada"),
    ("en_NZ", "English - New Zealand"),
    ("en_IE", "English - Ireland"),
    ("en_ZA", "English - South Africa"),
    ("en_JA", "English - Jamaica"),
    ("en_CB", "English - Carribbean"),
    ("en_BZ", "English - Belize"),
    ("en_TT", "English - Trinidad"),
    ("en_ZW", "English - Zimbabwe"),
    ("en_PH", "English - Philippines"),
    ("en_IN", "English - India"),
    ("en_MY", "English - Malaysia"),
    ("en_IN", "English - Singapore"),
    ("et_EE", "Estonian"),
    ("fo_FO", "Faroese"),
    ("fil_PH", "Filipino"),
    ("fi_FI", "Finnish"),
    ("fr_FR", "French - France"),
    ("fr_BE", "French - Belgium"),
    ("fr_CA", "French - Canada"),
    ("fr_CH", "French - Switzerland"),
    ("fr_LU", "French - Luxembourg"),
    ("fr_MC", "French - Monaco"),
    ("fy_NL", "Frisian - Netherlands"),
    ("gl_ES", "Galician"),
    ("ka_GE", "Georgian"),
    ("de_DE", "German - Germany"),
    ("de_CH", "German - Switzerland"),
    ("de_AT", "German - Austria"),
    ("de_LU", "German - Luxembourg"),
    ("de_LI", "German - Liechtenstein"),
    ("el_GR", "Greek"),
    ("kl_GL", "Greenlandic - Greenland"),
    ("gu_IN", "Gujarati"),
    ("ha_NG", "Hausa - Latin"),
    ("he_IL", "Hebrew"),
    ("hi_IN", "Hindi"),
    ("hu_HU", "Hungarian"),
    ("is_IS", "Icelandic"),
    ("id_ID", "Indonesian"),
    ("iu_CA", "Inuktitut - Syllabics"),
    ("iu_CA", "Inuktitut - Latin"),
    ("ga_IE", "Irish - Ireland"),
    ("it_IT", "Italian - Italy"),
    ("it_CH", "Italian - Switzerland"),
    ("ja_JP", "Japanese"),
    ("kn_IN", "Kannada - India"),
    ("kk_KZ", "Kazakh"),
    ("kh_KH", "Khmer - Cambodia"),
    ("qut_GT", "K'iche - Guatemala"),
    ("rw_RW", "Kinyarwanda - Rwanda"),
    ("kok_IN", "Konkani"),
    ("ko_KR", "Korean"),
    ("ky_KG", "Kyrgyz"),
    ("lo_LA", "Lao - Lao PDR"),
    ("lv_LV", "Latvian"),
    ("lt_LT", "Lithuanian"),
    ("dsb_DE", "Lower Sorbian - Germany"),
    ("lb_LU", "Luxembourgish"),
    ("mk_MK", "FYROM Macedonian"),
    ("ms_MY", "Malay - Malaysia"),
    ("ms_BN", "Malay - Brunei Darussalam"),
    ("ml_IN", "Malayalam - India"),
    ("mt_MT", "Maltese"),
    ("mi_NZ", "Maori"),
    ("arn_CL", "Mapudungun"),
    ("mr_IN", "Marathi"),
    ("moh_CA", "Mohawk - Canada"),
    ("mn_MN", "Mongolian - Cyrillic"),
    ("mn_CN", "Mongolian - PRC"),
    ("ne_NP", "Nepali"),
    ("nb_NO", "Norwegian - Bokmal"),
    ("nn_NO", "Norwegian - Nynorsk"),
    ("oc_FR", "Occitan - France"),
    ("or_IN", "Oriya - India"),
    ("ps_AF", "Pashto - Afghanistan"),
    ("fa_IR", "Persian"),
    ("pl_PL", "Polish"),
    ("pt_BR", "Portuguese - Brazil"),
    ("pt_PT", "Portuguese - Portugal"),
    ("pa_IN", "Punjabi"),
    ("quz_BO", "Quechua (Bolivia)"),
    ("quz_EC", "Quechua (Ecuador)"),
    ("quz_PE", "Quechua (Peru)"),
    ("ro_RO", "Romanian - Romania"),
    ("rm_CH", "Romansh"),
    ("ru_RU", "Russian"),
    ("smn_FI", "Sami Finland"),
    ("smj_NO", "Sami Norway"),
    ("smj_SE", "Sami Sweden"),
    ("se_NO", "Sami Northern Norway"),
    ("se_SE", "Sami Northern Sweden"),
    ("se_FI", "Sami Northern Finland"),
    ("sms_FI", "Sami Skolt"),
    ("sma_NO", "Sami Southern Norway"),
    ("sma_SE", "Sami Southern Sweden"),
    ("sa_IN", "Sanskrit"),
    ("sr_SP", "Serbian - Cyrillic"),
    ("sr_BA", "Serbian - Bosnia Cyrillic"),
    ("sr_SP", "Serbian - Latin"),
    ("sr_BA", "Serbian - Bosnia Latin"),
    ("si_LK", "Sinhala - Sri Lanka"),
    ("ns_ZA", "Northern Sotho"),
    ("tn_ZA", "Setswana - Southern Africa"),
    ("sk_SK", "Slovak"),
    ("sl_SI", "Slovenian"),
    ("es_ES", "Spanish - Spain"),
    ("es_MX", "Spanish - Mexico"),
    ("es_ES", "Spanish - Spain (Modern)"),
    ("es_GT", "Spanish - Guatemala"),
    ("es_CR", "Spanish - Costa Rica"),
    ("es_PA", "Spanish - Panama"),
    ("es_DO", "Spanish - Dominican Republic"),
    ("es_VE", "Spanish - Venezuela"),
    ("es_CO", "Spanish - Colombia"),
    ("es_PE", "Spanish - Peru"),
    ("es_AR", "Spanish - Argentina"),
    ("es_EC", "Spanish - Ecuador"),
    ("es_CL", "Spanish - Chile"),
    ("es_UR", "Spanish - Uruguay"),
    ("es_PY", "Spanish - Paraguay"),
    ("es_BO", "Spanish - Bolivia"),
    ("es_SV", "Spanish - El Salvador"),
    ("es_HN", "Spanish - Honduras"),
    ("es_NI", "Spanish - Nicaragua"),
    ("es_PR", "Spanish - Puerto Rico"),
    ("es_US", "Spanish - United States"),
    ("", "Sutu - Not supported"),
    ("sw_KE", "Swahili"),
    ("sv_SE", "Swedish - Sweden"),
    ("sv_FI", "Swedish - Finland"),
    ("syr_SY", "Syriac"),
    ("tg_TJ", "Tajik - Cyrillic"),
    ("tmz_DZ", "Tamazight - Latin"),
    ("ta_IN", "Tamil"),
    ("tt_RU", "Tatar"),
    ("te_IN", "Telugu"),
    ("th_TH", "Thai"),
    ("bo_BT", "Tibetan - Bhutan"),
    ("bo_CN", "Tibetan - PRC"),
    ("tr_TR", "Turkish"),
    ("tk_TM", "Turkmen - Cyrillic"),
    ("ug_CN", "Uighur - Arabic"),
    ("uk_UA", "Ukrainian"),
    ("wen_DE", "Upper Sorbian - Germany"),
    ("ur_PK", "Urdu"),
    ("ur_IN", "Urdu - India"),
    ("uz_UZ", "Uzbek - Latin"),
    ("uz_UZ", "Uzbek - Cyrillic"),
    ("vi_VN", "Vietnamese"),
    ("cy_GB", "Welsh"),
    ("wo_SN", "Wolof - Senegal"),
    ("xh_ZA", "Xhosa - South Africa"),
    ("sah_RU", "Yakut - Cyrillic"),
    ("ii_CN", "Yi - PRC"),
    ("yo_NG", "Yoruba - Nigeria"),
    ("zu_ZA", "Zulu"),
]

for code, place in locales:
    print('{:>6} : {}'.format(code, place))
