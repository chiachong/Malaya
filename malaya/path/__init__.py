from malaya import home

MALAY_TEXT = home + '/dictionary/malay-text.txt'
MALAY_TEXT_200K = home + '/dictionary-200k/malay-text.txt'

# sorted based on modules, started from augmentation until toxic

PATH_AUGMENTATION = {
    'synonym': {
        'model': home + '/synonym/synonym0.json',
        'model2': home + '/synonym/synonym1.json',
        'version': 'v35',
    }
}

S3_PATH_AUGMENTATION = {
    'synonym': {
        'model': 'https://raw.githubusercontent.com/huseinzol05/Malaya-Dataset/master/dictionary/synonym/synonym0.json',
        'model2': 'https://raw.githubusercontent.com/huseinzol05/Malaya-Dataset/master/dictionary/synonym/synonym1.json',
    }
}

# dependency.py
PATH_DEPENDENCY = {
    'bert': {
        'model': home + '/dependency/bert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'tiny-bert': {
        'model': home + '/dependency/bert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'albert': {
        'model': home + '/dependency/albert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'tiny-albert': {
        'model': home + '/dependency/albert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'xlnet': {
        'model': home + '/dependency/xlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'version': 'v34',
    },
    'alxlnet': {
        'model': home + '/dependency/alxlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'version': 'v34',
    },
}

S3_PATH_DEPENDENCY = {
    'bert': {
        'model': 'v34/dependency/bert-base-dependency.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'tiny-bert': {
        'model': 'v34/dependency/tiny-bert-dependency.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'albert': {
        'model': 'v34/dependency/albert-base-dependency.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'tiny-albert': {
        'model': 'v34/dependency/albert-tiny-dependency.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'xlnet': {
        'model': 'v34/dependency/xlnet-base-dependency.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
    'alxlnet': {
        'model': 'v34/dependency/alxlnet-base-dependency.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
}

PATH_EMOTION = {
    'multinomial': {
        'model': home + '/emotion/multinomial/multinomial.pkl',
        'vector': home + '/emotion/multinomial/tfidf.pkl',
        'bpe': home + '/emotion/multinomial/bpe.model',
        'version': 'v34',
    },
    'bert': {
        'model': home + '/emotion/bert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'tiny-bert': {
        'model': home + '/emotion/bert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'albert': {
        'model': home + '/emotion/albert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'tiny-albert': {
        'model': home + '/emotion/albert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'xlnet': {
        'model': home + '/emotion/xlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'version': 'v34',
    },
    'alxlnet': {
        'model': home + '/emotion/alxlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'version': 'v34',
    },
}

S3_PATH_EMOTION = {
    'multinomial': {
        'model': 'v34/emotion/multinomial.pkl',
        'vector': 'v34/emotion/tfidf.pkl',
        'bpe': 'v34/emotion/bpe.model',
    },
    'bert': {
        'model': 'v34/emotion/bert-base-emotion.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'tiny-bert': {
        'model': 'v34/emotion/tiny-bert-emotion.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'albert': {
        'model': 'v34/emotion/albert-base-emotion.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'tiny-albert': {
        'model': 'v34/emotion/albert-tiny-emotion.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'xlnet': {
        'model': 'v34/emotion/xlnet-base-emotion.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
    'alxlnet': {
        'model': 'v34/emotion/alxlnet-base-emotion.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
}

PATH_ENTITIES = {
    'bert': {
        'model': home + '/entity/bert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'setting': home + '/entity/dictionary-entities.json',
        'version': 'v34',
    },
    'tiny-bert': {
        'model': home + '/entity/bert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'setting': home + '/entity/dictionary-entities.json',
        'version': 'v34',
    },
    'albert': {
        'model': home + '/entity/albert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'setting': home + '/entity/dictionary-entities.json',
        'version': 'v34',
    },
    'tiny-albert': {
        'model': home + '/entity/albert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'setting': home + '/entity/dictionary-entities.json',
        'version': 'v34',
    },
    'xlnet': {
        'model': home + '/entity/xlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'setting': home + '/entity/dictionary-entities.json',
        'version': 'v34',
    },
    'alxlnet': {
        'model': home + '/entity/alxlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'setting': home + '/entity/dictionary-entities.json',
        'version': 'v34',
    },
}

S3_PATH_ENTITIES = {
    'bert': {
        'model': 'v34/entity/bert-base-entity.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
        'setting': 'bert-bahasa/dictionary-entities.json',
    },
    'tiny-bert': {
        'model': 'v34/entity/tiny-bert-entity.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
        'setting': 'bert-bahasa/dictionary-entities.json',
    },
    'albert': {
        'model': 'v34/entity/albert-base-entity.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
        'setting': 'bert-bahasa/dictionary-entities.json',
    },
    'tiny-albert': {
        'model': 'v34/entity/albert-tiny-entity.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
        'setting': 'bert-bahasa/dictionary-entities.json',
    },
    'xlnet': {
        'model': 'v34/entity/xlnet-base-entity.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
        'setting': 'bert-bahasa/dictionary-entities.json',
    },
    'alxlnet': {
        'model': 'v34/entity/alxlnet-base-entity.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
        'setting': 'bert-bahasa/dictionary-entities.json',
    },
}

PATH_GENERATOR = {
    'sample': {
        'base': {
            'path': home + '/generator-sample/t5/base',
            'directory': home + '/generator-sample/t5/base/model/',
            'model': {
                'model': home
                + '/generator-sample/t5/base/generator-t5-base.tar.gz',
                'version': 'v35',
            },
        },
        'small': {
            'path': home + '/generator-sample/t5/small',
            'directory': home + '/generator-sample/t5/small/model/',
            'model': {
                'model': home
                + '/generator-sample/t5/small/generator-t5-small.tar.gz',
                'version': 'v35',
            },
        },
    }
}

S3_PATH_GENERATOR = {
    'sample': {
        'base': {'model': 'v35/generator/sample-generator-t5-base.tar.gz'},
        'small': {'model': 'v35/generator/sample-generator-t5-small.tar.gz'},
    }
}

PATH_LANG_DETECTION = {
    'fasttext-original': {
        'model': home + '/language-detection/fasttext-original/fasstext.bin',
        'version': 'v34',
    },
    'fasttext-quantized': {
        'model': home + '/language-detection/fasttext-quantized/fasstext.tfz',
        'version': 'v34',
    },
    'deep': {
        'model': home
        + '/language-detection/deep/model.ckpt.data-00000-of-00001',
        'index': home + '/language-detection/deep/model.ckpt.index',
        'meta': home + '/language-detection/deep/model.ckpt.meta',
        'vector': home
        + '/language-detection/deep/vectorizer-language-detection.pkl',
        'bpe': home + '/language-detection/deep/bpe.model',
        'version': 'v34',
    },
}

S3_PATH_LANG_DETECTION = {
    'fasttext-original': {
        'model': 'v34/language-detection/fasttext-malaya.bin'
    },
    'fasttext-quantized': {
        'model': 'v34/language-detection/fasttext-malaya.ftz'
    },
    'deep': {
        'model': 'v34/language-detection/model.ckpt.data-00000-of-00001',
        'index': 'v34/language-detection/model.ckpt.index',
        'meta': 'v34/language-detection/model.ckpt.meta',
        'vector': 'v34/language-detection/bow-language-detection.pkl',
        'bpe': 'v34/language-detection/language-detection.model',
    },
}

PATH_NGRAM = {
    1: {
        'model': home + '/preprocessing/ngram1/bm_1grams.json',
        'version': 'v28',
    },
    2: {
        'model': home + '/preprocessing/ngram2/bm_2grams.json',
        'version': 'v23',
    },
    'symspell': {
        'model': home + '/preprocessing/symspell/bm_1grams.txt',
        'version': 'v28',
    },
    'sentencepiece': {
        'vocab': home + '/preprocessing/sentencepiece/sp10m.cased.v4.vocab',
        'model': home + '/preprocessing/sentencepiece/sp10m.cased.v4.model',
        'version': 'v31',
    },
}

S3_PATH_NGRAM = {
    1: {'model': 'v27/preprocessing/bm_1grams.json'},
    2: {'model': 'v23/preprocessing/bm_2grams.json'},
    'symspell': {'model': 'v27/preprocessing/bm_1grams.txt'},
    'sentencepiece': {
        'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
        'model': 'bert-bahasa/sp10m.cased.v4.model',
    },
}

PATH_POS = {
    'bert': {
        'model': home + '/pos/bert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'setting': home + '/pos/dictionary-pos.json',
        'version': 'v34',
    },
    'tiny-bert': {
        'model': home + '/pos/bert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'setting': home + '/pos/dictionary-pos.json',
        'version': 'v34',
    },
    'albert': {
        'model': home + '/pos/albert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'setting': home + '/pos/dictionary-pos.json',
        'version': 'v34',
    },
    'tiny-albert': {
        'model': home + '/pos/albert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'setting': home + '/pos/dictionary-pos.json',
        'version': 'v34',
    },
    'xlnet': {
        'model': home + '/pos/xlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'setting': home + '/pos/dictionary-pos.json',
        'version': 'v34',
    },
    'alxlnet': {
        'model': home + '/pos/alxlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'setting': home + '/pos/dictionary-pos.json',
        'version': 'v34',
    },
}

S3_PATH_POS = {
    'bert': {
        'model': 'v34/pos/bert-base-pos.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
        'setting': 'bert-bahasa/dictionary-pos.json',
    },
    'tiny-bert': {
        'model': 'v34/pos/tiny-bert-pos.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
        'setting': 'bert-bahasa/dictionary-pos.json',
    },
    'albert': {
        'model': 'v34/pos/albert-base-pos.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
        'setting': 'bert-bahasa/dictionary-pos.json',
    },
    'tiny-albert': {
        'model': 'v34/pos/albert-tiny-pos.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
        'setting': 'bert-bahasa/dictionary-pos.json',
    },
    'xlnet': {
        'model': 'v34/pos/xlnet-base-pos.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
        'setting': 'bert-bahasa/dictionary-pos.json',
    },
    'alxlnet': {
        'model': 'v34/pos/alxlnet-base-pos.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
        'setting': 'bert-bahasa/dictionary-pos.json',
    },
}

PATH_PREPROCESSING = {
    1: {
        'model': home + '/preprocessing/count1/1counts_1grams.json',
        'version': 'v23',
    },
    2: {
        'model': home + '/preprocessing/count2/counts_2grams.json',
        'version': 'v23',
    },
    'english-malay': {
        'model': home + '/preprocessing/english-malay/english-malay-200k.json',
        'version': 'v23',
    },
}

S3_PATH_PREPROCESSING = {
    1: {'model': 'v23/preprocessing/counts_1grams.json'},
    2: {'model': 'v23/preprocessing/counts_2grams.json'},
    'english-malay': {'model': 'v23/preprocessing/english-malay-200k.json'},
}

PATH_RELEVANCY = {
    'bert': {
        'model': home + '/relevancy/bert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'tiny-bert': {
        'model': home + '/relevancy/bert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'albert': {
        'model': home + '/relevancy/albert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'tiny-albert': {
        'model': home + '/relevancy/albert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'xlnet': {
        'model': home + '/relevancy/xlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'version': 'v34',
    },
    'alxlnet': {
        'model': home + '/relevancy/alxlnet/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v9.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v9.model',
        'version': 'v34',
    },
}
S3_PATH_RELEVANCY = {
    'bert': {
        'model': 'v34/relevancy/bert-base-relevancy.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'tiny-bert': {
        'model': 'v34/relevancy/tiny-bert-relevancy.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'albert': {
        'model': 'v34/relevancy/albert-base-relevancy.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'tiny-albert': {
        'model': 'v34/relevancy/albert-tiny-relevancy.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'xlnet': {
        'model': 'v34/relevancy/xlnet-base-relevancy.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
    'alxlnet': {
        'model': 'v34/relevancy/alxlnet-base-relevancy.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
}

PATH_SENTIMENT = {
    'multinomial': {
        'model': home + '/sentiment/multinomial/multinomial.pkl',
        'vector': home + '/sentiment/multinomial/tfidf.pkl',
        'bpe': home + '/sentiment/multinomial/bpe.model',
        'version': 'v34',
    },
    'bert': {
        'model': home + '/sentiment/bert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'tiny-bert': {
        'model': home + '/sentiment/bert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'albert': {
        'model': home + '/sentiment/albert/base/model.pb',
        'vocab': home + '/albert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/albert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'tiny-albert': {
        'model': home + '/sentiment/albert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'xlnet': {
        'model': home + '/sentiment/xlnet/base/model.pb',
        'vocab': home + '/xlnet/sp10m.cased.v9.vocab',
        'tokenizer': home + '/xlnet/sp10m.cased.v9.model',
        'version': 'v34',
    },
    'alxlnet': {
        'model': home + '/sentiment/alxlnet/base/model.pb',
        'vocab': home + '/xlnet/sp10m.cased.v9.vocab',
        'tokenizer': home + '/xlnet/sp10m.cased.v9.model',
        'version': 'v34',
    },
}

S3_PATH_SENTIMENT = {
    'multinomial': {
        'model': 'v34/sentiment/multinomial.pkl',
        'vector': 'v34/sentiment/tfidf.pkl',
        'bpe': 'v34/sentiment/bpe.model',
    },
    'bert': {
        'model': 'v34/sentiment/bert-base-sentiment.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'tiny-bert': {
        'model': 'v34/sentiment/tiny-bert-sentiment.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'albert': {
        'model': 'v34/sentiment/albert-base-sentiment.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'tiny-albert': {
        'model': 'v34/sentiment/albert-tiny-sentiment.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'xlnet': {
        'model': 'v34/sentiment/xlnet-base-sentiment.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
    'alxlnet': {
        'model': 'v34/sentiment/alxlnet-base-sentiment.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
}

PATH_SIMILARITY = {
    'bert': {
        'model': home + '/similarity/bert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'tiny-bert': {
        'model': home + '/similarity/bert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'albert': {
        'model': home + '/similarity/albert/base/model.pb',
        'vocab': home + '/albert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/albert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'tiny-albert': {
        'model': home + '/similarity/albert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'xlnet': {
        'model': home + '/similarity/xlnet/base/model.pb',
        'vocab': home + '/xlnet/sp10m.cased.v9.vocab',
        'tokenizer': home + '/xlnet/sp10m.cased.v9.model',
        'version': 'v34',
    },
    'alxlnet': {
        'model': home + '/similarity/alxlnet/base/model.pb',
        'vocab': home + '/xlnet/sp10m.cased.v9.vocab',
        'tokenizer': home + '/xlnet/sp10m.cased.v9.model',
        'version': 'v34',
    },
}

S3_PATH_SIMILARITY = {
    'bert': {
        'model': 'v34/similarity/bert-base-similarity.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'tiny-bert': {
        'model': 'v34/similarity/tiny-bert-similarity.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'albert': {
        'model': 'v34/similarity/albert-base-similarity.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'tiny-albert': {
        'model': 'v34/similarity/albert-tiny-similarity.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'xlnet': {
        'model': 'v34/similarity/xlnet-base-similarity.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
    'alxlnet': {
        'model': 'v34/similarity/alxlnet-base-similarity.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
}

PATH_STEM = {
    'deep': {
        'model': home + '/stem/lstm/model.pb',
        'bpe': home + '/stem/lstm/bpe.model',
        'version': 'v34',
    }
}

S3_PATH_STEM = {
    'deep': {'model': 'v34/stem/model.pb', 'bpe': 'v34/stem/bpe.model'}
}

PATH_SUBJECTIVE = {
    'multinomial': {
        'model': home + '/subjective/multinomial/multinomial.pkl',
        'vector': home + '/subjective/multinomial/tfidf.pkl',
        'bpe': home + '/subjective/multinomial/bpe.model',
        'version': 'v34',
    },
    'bert': {
        'model': home + '/subjective/bert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'tiny-bert': {
        'model': home + '/subjective/bert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'albert': {
        'model': home + '/subjective/albert/base/model.pb',
        'vocab': home + '/albert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/albert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'tiny-albert': {
        'model': home + '/subjective/albert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'xlnet': {
        'model': home + '/subjective/xlnet/base/model.pb',
        'vocab': home + '/xlnet/sp10m.cased.v9.vocab',
        'tokenizer': home + '/xlnet/sp10m.cased.v9.model',
        'version': 'v34',
    },
    'alxlnet': {
        'model': home + '/subjective/alxlnet/base/model.pb',
        'vocab': home + '/xlnet/sp10m.cased.v9.vocab',
        'tokenizer': home + '/xlnet/sp10m.cased.v9.model',
        'version': 'v34',
    },
}

S3_PATH_SUBJECTIVE = {
    'multinomial': {
        'model': 'v34/subjective/multinomial.pkl',
        'vector': 'v34/subjective/tfidf.pkl',
        'bpe': 'v34/subjective/bpe.model',
    },
    'bert': {
        'model': 'v34/subjective/bert-base-subjective.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'tiny-bert': {
        'model': 'v34/subjective/tiny-bert-subjective.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'albert': {
        'model': 'v34/subjective/albert-base-subjective.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'tiny-albert': {
        'model': 'v34/subjective/albert-tiny-subjective.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'xlnet': {
        'model': 'v34/subjective/xlnet-base-subjective.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
    'alxlnet': {
        'model': 'v34/subjective/alxlnet-base-subjective.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
}

PATH_SUMMARIZE = {
    'news': {
        'model': home + '/summarize/summary-news.pb',
        'setting': home + '/summarize/summary-news.json',
        'version': 'v13',
    },
    'wiki': {
        'model': home + '/summarize/summary-wiki.pb',
        'setting': home + '/summarize/summary-wiki.json',
        'version': 'v13',
    },
    'argmax': {
        'base': {
            'path': home + '/summarize-argmax/t5/base',
            'directory': home + '/summarize-argmax/t5/base/model/',
            'model': {
                'model': home
                + '/summarize-argmax/t5/base/summarize-t5-base.tar.gz',
                'version': 'v35',
            },
        }
    },
}

S3_PATH_SUMMARIZE = {
    'news': {
        'model': 'v13/summarize/summary-news.pb',
        'setting': 'v13/summarize/summary-news.json',
    },
    'wiki': {
        'model': 'v13/summarize/summary-wiki.pb',
        'setting': 'v13/summarize/summary-wiki.json',
    },
    'argmax': {
        'base': {'model': 'v35/summarize/argmax-summarize-t5-base.tar.gz'}
    },
}

PATH_TOXIC = {
    'multinomial': {
        'model': home + '/toxicity/multinomial/multinomial.pkl',
        'vector': home + '/toxicity/multinomial/tfidf.pkl',
        'bpe': home + '/toxicity/multinomial/bpe.model',
        'version': 'v34',
    },
    'bert': {
        'model': home + '/toxicity/bert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'tiny-bert': {
        'model': home + '/toxicity/bert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.bert.vocab',
        'tokenizer': home + '/bert/sp10m.cased.bert.model',
        'version': 'v34',
    },
    'albert': {
        'model': home + '/toxicity/albert/base/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'tiny-albert': {
        'model': home + '/toxicity/albert/tiny/model.pb',
        'vocab': home + '/bert/sp10m.cased.v10.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v10.model',
        'version': 'v34',
    },
    'xlnet': {
        'model': home + '/toxicity/xlnet/base/model.pb',
        'vocab': home + '/xlnet/sp10m.cased.v9.vocab',
        'tokenizer': home + '/xlnet/sp10m.cased.v9.model',
        'version': 'v34',
    },
    'alxlnet': {
        'model': home + '/toxicity/alxlnet/base/model.pb',
        'vocab': home + '/alxlnet/sp10m.cased.v9.vocab',
        'tokenizer': home + '/alxlnet/sp10m.cased.v9.model',
        'version': 'v34',
    },
}

S3_PATH_TOXIC = {
    'multinomial': {
        'model': 'v34/toxicity/multinomial.pkl',
        'vector': 'v34/toxicity/tfidf.pkl',
        'bpe': 'v34/toxicity/bpe.model',
    },
    'bert': {
        'model': 'v34/toxicity/bert-base-toxicity.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'tiny-bert': {
        'model': 'v34/toxicity/tiny-bert-toxicity.pb',
        'vocab': 'tokenizer/sp10m.cased.bert.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.bert.model',
    },
    'albert': {
        'model': 'v34/toxicity/albert-base-toxicity.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'tiny-albert': {
        'model': 'v34/toxicity/albert-tiny-toxicity.pb',
        'vocab': 'tokenizer/sp10m.cased.v10.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v10.model',
    },
    'xlnet': {
        'model': 'v34/toxicity/xlnet-base-toxicity.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
    'alxlnet': {
        'model': 'v34/toxicity/alxlnet-base-toxicity.pb',
        'vocab': 'tokenizer/sp10m.cased.v9.vocab',
        'tokenizer': 'tokenizer/sp10m.cased.v9.model',
    },
}

PATH_ELECTRA = {
    'electra': {
        'path': home + '/electra-model/base',
        'directory': home + '/electra-model/base/electra-base/',
        'model': {
            'model': home + '/electra-model/base/electra-bahasa-base.tar.gz',
            'version': 'v34',
        },
    },
    'small-electra': {
        'path': home + '/electra-model/small',
        'directory': home + '/electra-model/small/electra-small/',
        'model': {
            'model': home + '/electra-model/small/electra-bahasa-small.tar.gz',
            'version': 'v34',
        },
    },
}

S3_PATH_ELECTRA = {
    'electra': {'model': 'v34/pretrained-model/electra-base.tar.gz'},
    'small-electra': {'model': 'v34/pretrained-model/electra-small.tar.gz'},
}

PATH_BERT = {
    'bert': {
        'path': home + '/bert-model/base',
        'directory': home + '/bert-model/base/bert-base-v3/',
        'model': {
            'model': home + '/bert-model/tiny/bert-bahasa-base.tar.gz',
            'version': 'v34',
        },
    },
    'tiny-bert': {
        'path': home + '/bert-model/tiny',
        'directory': home + '/bert-model/tiny/tiny-bert-v1/',
        'model': {
            'model': home + '/bert-model/base/tiny-bert-bahasa.tar.gz',
            'version': 'v34',
        },
    },
}

S3_PATH_BERT = {
    'bert': {'model': 'v34/pretrained-model/bert-base.tar.gz'},
    'tiny-bert': {'model': 'v34/pretrained-model/tiny-bert.tar.gz'},
}

PATH_ALBERT = {
    'albert': {
        'path': home + '/albert-model/base',
        'directory': home + '/albert-model/base/albert-base/',
        'model': {
            'model': home + '/albert-model/base/albert-bahasa-base.tar.gz',
            'version': 'v34',
        },
    },
    'tiny-albert': {
        'path': home + '/albert-model/tiny',
        'directory': home + '/albert-model/tiny/albert-tiny/',
        'model': {
            'model': home + '/albert-model/tiny/albert-bahasa-tiny.tar.gz',
            'version': 'v34',
        },
    },
}

S3_PATH_ALBERT = {
    'albert': {'model': 'v34/pretrained-model/albert-base.tar.gz'},
    'tiny-albert': {'model': 'v34/pretrained-model/albert-tiny.tar.gz'},
}

PATH_XLNET = {
    'xlnet': {
        'path': home + '/xlnet-model/base',
        'directory': home + '/xlnet-model/base/xlnet-base/',
        'model': {
            'model': home + '/xlnet-model/base/xlnet-base.tar.gz',
            'version': 'v34',
        },
    }
}

S3_PATH_XLNET = {'xlnet': {'model': 'v34/pretrained-model/xlnet-base.tar.gz'}}

PATH_ALXLNET = {
    'alxlnet': {
        'path': home + '/alxlnet-model/base',
        'directory': home + '/alxlnet-model/base/alxlnet-base/',
        'model': {
            'model': home + '/alxlnet-model/base/alxlnet-base.tar.gz',
            'version': 'v34',
        },
    }
}

S3_PATH_ALXLNET = {
    'alxlnet': {'model': 'v34/pretrained-model/alxlnet-base.tar.gz'}
}

PATH_GPT2 = {
    '117M': {
        'path': home + '/gpt2/117M/',
        'directory': home + '/gpt2/117M/gpt2-bahasa-117M/',
        'model': {
            'model': home + '/gpt2/117M/gpt2-117M.tar.gz',
            'version': 'v34',
        },
    },
    '345M': {
        'path': home + '/gpt2/345M/',
        'directory': home + '/gpt2/345M/gpt2-bahasa-345M/',
        'model': {
            'model': home + '/gpt2/345M/gpt2-345M.tar.gz',
            'version': 'v34',
        },
    },
}

S3_PATH_GPT2 = {
    '117M': {'model': 'v34/pretrained-model/gpt2-bahasa-117M.tar.gz'},
    '345M': {'model': 'v34/pretrained-model/gpt2-bahasa-345M.tar.gz'},
}

PATH_WORDVECTOR = {
    'news': {
        'vocab': home + '/wordvector/news/wordvector.json',
        'model': home + '/wordvector/news/wordvector.npy',
        'version': 'v31',
    },
    'wikipedia': {
        'vocab': home + '/wordvector/wikipedia/wordvector.json',
        'model': home + '/wordvector/wikipedia/wordvector.npy',
        'version': 'v31',
    },
    'socialmedia': {
        'vocab': home + '/wordvector/socialmedia/wordvector.json',
        'model': home + '/wordvector/socialmedia/wordvector.npy',
        'version': 'v31',
    },
    'combine': {
        'vocab': home + '/wordvector/combine/wordvector.json',
        'model': home + '/wordvector/combine/wordvector.npy',
        'version': 'v34',
    },
}

S3_PATH_WORDVECTOR = {
    'news': {
        'vocab': 'bert-bahasa/word2vec-news-ms-256.json',
        'model': 'bert-bahasa/word2vec-news-ms-256.npy',
    },
    'wikipedia': {
        'vocab': 'bert-bahasa/word2vec-wiki-ms-256.json',
        'model': 'bert-bahasa/word2vec-wiki-ms-256.npy',
    },
    'socialmedia': {
        'vocab': 'bert-bahasa/word2vec-ms-socialmedia-256.json',
        'model': 'bert-bahasa/word2vec-ms-socialmedia-256.npy',
    },
    'combine': {
        'vocab': 'bert-bahasa/word2vec-combined-256.json',
        'model': 'bert-bahasa/word2vec-combined-256.npy',
    },
}
