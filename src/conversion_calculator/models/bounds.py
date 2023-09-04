from pydantic import BaseModel, Field, root_validator


class ValueBounds(BaseModel):
    min_value: int = Field(..., ge=0)
    max_value: int = Field(..., gt=0)

    @root_validator
    def check_bounds(cls, values):
        if values.get("min_value") == values.get("max_value"):
            raise ValueError("min_value must be less than max_value")


min_values = {
    "cvlt_form": 0,
    "cvlt_imfr_t1_c": 0,
    "cvlt_imfr_t2_c": 0,
    "cvlt_imfr_t3_c": 0,
    "cvlt_imfr_t4_c": 0,
    "cvlt_imfr_t5_c": 0,
    "cvlt_imfr_t15_total": 0,
    "cvlt_imfr_b_c": 0,
    "cvlt_sdfr_c": 0,
    "cvlt_sdcr_c": 0,
    "cvlt_ldfr_c": 0,
    "cvlt_ldcr_c": 0,
    "cvlt_rep_tot": 0,
    "cvlt_int_tot": 0,
    "cvlt_recog_hits": 0,
    "cvlt_recog_fp": 0,
    "cvltc_imfr_t1_c": 0,
    "cvltc_imfr_t2_c": 0,
    "cvltc_imfr_t3_c": 0,
    "cvltc_imfr_t4_c": 0,
    "cvltc_imfr_t5_c": 0,
    "cvltc_imfr_t15_total": 0,
    "cvltc_imfr_tb_c": 0,
    "cvltc_sdfr_c": 0,
    "cvltc_sdcr_c": 0,
    "cvltc_ldfr_c": 0,
    "cvltc_ldcr_c": 0,
    "cvltc_recog_hits": 0,
    "ravlt_form": 0,
    "ravlt_imfr_t1_c": 0,
    "ravlt_imfr_t1_i": 0,
    "ravlt_imfr_t2_c": 0,
    "ravlt_imfr_t2_i": 0,
    "ravlt_imfr_t3_c": 0,
    "ravlt_imfr_t3_i": 0,
    "ravlt_imfr_t4_c": 0,
    "ravlt_imfr_t4_i": 0,
    "ravlt_imfr_t5_c": 0,
    "ravlt_imfr_t5_i": 0,
    "ravlt_imfr_t15_total": 0,
    "ravlt_imfr_b_c": 0,
    "ravlt_imfr_b_i": 0,
    "ravlt_sdfr_c": 0,
    "ravlt_sdfr_i": 0,
    "ravlt_ldfr_c": 0,
    "ravlt_ldfr_i": 0,
    "ravlt_recog_hits": 0,
    "hvlt_version": 0,
    "hvlt_imfr_t1_c": 0,
    "hvlt_imfr_t2_c": 0,
    "hvlt_imfr_t3_c": 0,
    "hvlt_imfr_t13_total": 0,
    "hvlt_dr_c": 0,
    "hvlt_recog_hits": 0,
}
max_values = {
    "cvlt_form": 17,
    "cvlt_imfr_t1_c": 16,
    "cvlt_imfr_t2_c": 16,
    "cvlt_imfr_t3_c": 16,
    "cvlt_imfr_t4_c": 16,
    "cvlt_imfr_t5_c": 80,
    "cvlt_imfr_t15_total": 16,
    "cvlt_imfr_b_c": 16,
    "cvlt_sdfr_c": 16,
    "cvlt_sdcr_c": 16,
    "cvlt_ldfr_c": 16,
    "cvlt_int_tot": 16,
    "cvlt_recog_hits": 32,
    "cvlt_recog_fp": 15,
    "cvltc_imfr_t1_c": 15,
    "cvltc_imfr_t2_c": 15,
    "cvltc_imfr_t3_c": 15,
    "cvltc_imfr_t4_c": 15,
    "cvltc_imfr_t5_c": 75,
    "cvltc_imfr_t15_total": 15,
    "cvltc_imfr_tb_c": 15,
    "cvltc_sdfr_c": 15,
    "cvltc_sdcr_c": 15,
    "cvltc_ldfr_c": 15,
    "cvltc_ldcr_c": 15,
    "cvltc_recog_hits": 30,
    "ravlt_form": 16,
    "ravlt_imfr_t1_i": 16,
    "ravlt_imfr_t2_i": 16,
    "ravlt_imfr_t3_i": 16,
    "ravlt_imfr_t4_i": 16,
    "ravlt_imfr_t5_i": 75,
    "ravlt_imfr_t15_total": 16,
    "ravlt_imfr_b_i": 16,
    "ravlt_sdfr_i": 16,
    "ravlt_ldfr_i": 15,
    "ravlt_ldfr_c": 15,
    "ravlt_recog_hits": 36,
    "hvlt_version": 12,
    "hvlt_imfr_t1_c": 12,
    "hvlt_imfr_t2_c": 12,
    "hvlt_imfr_t3_c": 36,
    "hvlt_imfr_t13_total": 12,
    "hvlt_dr_c": 12,
    "hvlt_recog_hits": 12,
}
